"""
build.py

Compiles everything down
"""
import argparse
import pathlib
import shlex
import shutil
import subprocess
import sys
import typing

import miko
from rich.prompt import Confirm
from rich.progress import Progress

import translatepy
from translatepy import logger


def subprocess_exec(command: typing.Union[str, typing.Iterable[str]],
                    required: bool = True,
                    steps: typing.Optional[typing.List[str]] = None, **kwargs) -> subprocess.Popen:
    """Executes the given command list"""
    steps = steps or []
    if isinstance(command, str):
        commands = shlex.split(command)
    else:
        commands = [str(com) for com in command]
    try:
        with Progress(console=logger._rich_console, transient=True) as progress:
            main_task = progress.add_task(f"Executing: `{' '.join(commands)}`", total=len(steps) if steps else None)

            def advances(line: bytes) -> bool:
                for step in steps.copy():
                    if step in line:
                        steps.remove(step)
                        return True
                return False

            logger.log(f"Executing: `{' '.join(commands)}`")
            with subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, **kwargs) as proc:
                for line in proc.stdout:
                    if isinstance(line, bytes):
                        line = line.decode()
                    if advances(line):
                        progress.advance(main_task)
                    progress.console.print(line, end="")
            # process = subprocess.run(commands, stdout=sys.stdout, stderr=sys.stderr, check=True, **kwargs)
            progress.console.print(f'[{commands!r} exited with {proc.returncode}]')
            if required and proc.returncode:
                logger.debug("")
                raise RuntimeError(f"An error occured while running `{' '.join(command)}`")
    except (subprocess.CalledProcessError, Exception) as ex:
        raise ValueError(f"While executing a process, an unknown error occurred: {ex}, command: {' '.join(command)}") from ex
    else:
        return proc


def test(verbose: bool = True, bypass: bool = False):
    """Tests translatepy"""
    logger.log("Testing `translatepy`")
    import pytest

    args = ["-vvs"] if verbose else []
    args.append("tests/")

    code = pytest.main(args)
    if code != 0 and not bypass:
        raise ValueError("Tests failed for `translatepy`")


def build_website(runtime: typing.Optional[str] = None):
    """Builds the website"""
    logger.log("Building the website for `translatepy`")
    runtime = runtime or shutil.which("bun") or shutil.which("npm") or shutil.which("yarn")
    if not runtime:
        logger.error("`bun`, `npm` or `yarn` is a website build dependency and doesn't seem to be installed on your system."
                     "Please install it before proceeding with the build process.")
        raise ModuleNotFoundError("Couldn't find `bun`, `npm` or `yarn`")

    website_dir = pathlib.Path(__file__).parent / "website"
    subprocess_exec([
        runtime, "install"
    ], cwd=website_dir)
    subprocess_exec(
        [runtime, "run", "build"],
        steps=[
            "Creating an optimized production build",
            "Compiled successfully",
            "Collecting page data",
            "inalizing page optimization",
            "automatically rendered as static HTML"
        ],
        cwd=website_dir
    )


def build_docs():
    """Builds the documentation"""
    logger.log("Building documentation")
    from nasse import localization as nasse_localization

    from translatepy.server.endpoints.api import _, language
    from translatepy.server.server import SERVER_DOCS_PATH

    docs_path = pathlib.Path(__file__).parent / "docs"

    def remove(directory: pathlib.Path):
        """Removes a file or a directory recursively"""
        try:
            (directory).unlink(missing_ok=True)
        except (IsADirectoryError, PermissionError):
            try:
                shutil.rmtree(directory)
            except Exception:
                pass
        except FileNotFoundError:
            pass

    logger.debug(f"Removing {SERVER_DOCS_PATH}")
    remove(SERVER_DOCS_PATH)

    logger.debug(f"Copying {docs_path} to {SERVER_DOCS_PATH}")
    shutil.copytree(str(docs_path), SERVER_DOCS_PATH)

    for language, localization in [(translatepy.ENGLISH, nasse_localization.EnglishLocalization),
                                   (translatepy.Language("french"), nasse_localization.FrenchLocalization),
                                   (translatepy.Language("japanese"), nasse_localization.JapaneseLocalization)]:

        logger.debug(f"Building server docs for `{language}`")

        # We can't just copy the result of `./docs` to `SERVER_DOCS_PATH/docs`
        # because `server.make_docs` produces different results following the
        # path given
        for path in [docs_path / str(language.id), SERVER_DOCS_PATH / str(language.id)]:
            path.mkdir(parents=True, exist_ok=True)

            remove(path / "server")
            translatepy.server.make_docs(path / "server", localization=localization)
            miko.markdown.make_docs(pathlib.Path(translatepy.__file__), path / "reference")

    logger.debug(f"Copying the main README to {docs_path / translatepy.ENGLISH.id / 'README.md'}")
    shutil.copyfile(str(pathlib.Path(__file__).parent / "README.md"),
                    str(docs_path / translatepy.ENGLISH.id / "README.md"))


def build_binary(output: typing.Optional[str] = None, platform: typing.Optional[str] = None):
    """Builds the binaries for translatepy"""
    platform = (platform or sys.platform).lower()
    if platform == "linux":
        logger.log("Building binaries for Linux")
        nuitka = shutil.which("nuitka3")
        if not nuitka:
            logger.error("`nuitka` is a build dependency and doesn't seem to be installed on your system."
                         "Please install it before proceeding with the build process.")
            raise ModuleNotFoundError("Couldn't find `nuitka`")
        logger.debug("Building `translatepy`")
        subprocess_exec([
            nuitka, "--onefile", "--nofollow-import-to=pytest",
            "--include-data-dir=translatepy/data=translatepy/data",
            "--include-data-files=translatepy/cli/tui/app.css=translatepy/cli/tui/app.css",
            "--python-flag=isolated,nosite,-O",
            "--plugin-enable=anti-bloat,implicit-imports,data-files,pylint-warnings",
            "--warn-implicit-exceptions", "--warn-unusual-code", "--prefer-source-code",
            "--static-libpython=yes", output or "translatepy"
        ])
    elif platform == "darwin":
        logger.log("Building binaries for macOS")
        nuitka = shutil.which("nuitka3")
        if not nuitka:
            logger.error("`nuitka` is a build dependency and doesn't seem to be installed on your system."
                         "Please install it before proceeding with the build process.")
            raise ModuleNotFoundError("Couldn't find `nuitka`")
        logger.debug("Building `translatepy`")
        subprocess_exec([
            nuitka, "--onefile", "--nofollow-import-to=pytest",
            "--include-data-dir=translatepy/data=translatepy/data",
            "--include-data-files=translatepy/cli/tui/app.css=translatepy/cli/tui/app.css",
            "--python-flag=isolated,nosite,-O",
            "--plugin-enable=anti-bloat,implicit-imports,data-files,pylint-warnings",
            "--warn-implicit-exceptions", "--warn-unusual-code", "--prefer-source-code",
            # "--static-libpython=yes",
            output or "translatepy"
        ])
    elif platform == "win32":
        # logger.log("Building binaries for Windows")
        logger.error(f"We don't support building binaries for Windows yet.")
        raise ValueError("System not suitable for building binaries")
    else:
        logger.error(f"We don't support building binaries for {platform} yet.")
        raise ValueError("System not suitable for building binaries")


def build():
    """Builds translatepy"""
    logger.info("Building `translatepy`")
    poetry = shutil.which("poetry")
    if not poetry:
        logger.error("`poetry` is a build dependency and doesn't seem to be installed on your system."
                     "Please install it before proceeding with the build process.")
        raise ModuleNotFoundError("Couldn't find `poetry`")
    subprocess_exec([
        poetry, "export", "-f", "requirements.txt", "--output", "requirements.txt"
    ])
    subprocess_exec([
        poetry, "install"
    ])
    subprocess_exec([
        poetry, "build"
    ])


def release(yes: bool = False):
    """Releases translatepy"""
    logger.log("Releasing `translatepy`")
    poetry = shutil.which("poetry")
    if not poetry:
        logger.error("`poetry` is a build dependency and doesn't seem to be installed on your system."
                     "Please install it before proceeding with the build process.")
        raise ModuleNotFoundError("Couldn't find `poetry`")
    if not yes:
        confirmation = Confirm(f"Do you want to release `translatepy v{translatepy.__version__}` ?")
        if not confirmation:
            return
    subprocess_exec([
        poetry, "release"
    ])


def prepare_argparse(parser: argparse.ArgumentParser):
    """Prepares the given parser"""
    parser.add_argument("--debug", "-d", action="store_true")
    subparsers = parser.add_subparsers(dest="dev_action", description="The action to perform", required=True)

    def prepare_test_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the test argument parser"""
        parser.add_argument("--verbose-tests", "--verbose-pytest", "-vvs", action="store_true", help="To enable verbose logging from pytest (also enabled with --debug)")
        parser.add_argument("--bypass-tests", action="store_true", help="To continue even when the tests fail")
        return parser

    def prepare_website_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the website builder argument parser"""
        parser.add_argument("--website-runtime", action="store", help="The JavaScript runtime to use to build the website (npm, yarn, bun, etc.)", required=False)
        return parser

    def prepare_docs_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the docs builder argument parser"""
        return parser

    def prepare_binary_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the binary builder argument parser"""
        parser.add_argument("--binary-output", action="store", help="The output for the binary build", required=False)
        parser.add_argument("--binary-platform", action="store", help="To overwrite the platform check when building binaries (linux, darwin, win32, etc.)", required=False)
        return parser

    def prepare_build_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the build argument parser"""
        parser.add_argument("--skip-tests", action="store_true", help="Completely skips tests")
        return parser

    def prepare_release_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the release argument parser"""
        parser.add_argument("--yes", "-y", action="store_true", help="To answer `yes` to the confirmation prompt")
        return parser

    test_parser = subparsers.add_parser("test", help=test.__doc__)
    website_parser = subparsers.add_parser("website", help=build_website.__doc__)
    docs_parser = subparsers.add_parser("docs", help=build_docs.__doc__)
    binary_parser = subparsers.add_parser("binary", help=build_binary.__doc__)
    build_parser = subparsers.add_parser("build", help=build.__doc__)
    release_parser = subparsers.add_parser("release", help=release.__doc__)

    prepare_test_parser(test_parser)
    prepare_test_parser(build_parser)
    prepare_test_parser(release_parser)

    prepare_website_parser(website_parser)
    prepare_website_parser(build_parser)
    prepare_website_parser(release_parser)

    prepare_docs_parser(docs_parser)
    prepare_docs_parser(build_parser)
    prepare_docs_parser(release_parser)

    prepare_binary_parser(binary_parser)
    prepare_binary_parser(build_parser)
    prepare_binary_parser(release_parser)

    prepare_build_parser(build_parser)
    prepare_build_parser(release_parser)

    prepare_release_parser(release_parser)


def entry(args: argparse.Namespace):
    """The main entrypoint for translatepy's `dev` CLI"""
    logger.config.debug = args.debug

    # Library Management
    if args.dev_action in ("release", "build", "test"):
        if not (args.dev_action in ("release", "build") and args.skip_tests):
            test(verbose=args.verbose_tests or args.debug, bypass=args.bypass_tests)

    if args.dev_action in ("release", "build", "website"):
        build_website(runtime=args.website_runtime)

    if args.dev_action in ("release", "build", "docs"):
        build_docs()

    if args.dev_action in ("release", "build", "binary"):
        build_binary(output=args.binary_output, platform=args.binary_platform)

    if args.dev_action in ("release", "build"):
        build()

    if args.dev_action in ("release",):
        release(yes=args.yes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("translatepy build", description="translatepy helper to build the library")
    parser.add_argument("--version", "-v", action="version", version=translatepy.__version__)
    try:
        prepare_argparse(parser)
        entry(args=parser.parse_args())
    except Exception:
        logger.print_exception(show_locals=("--debug" in sys.argv or "-d" in sys.argv))
