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

import translatepy
from translatepy import logger


def subprocess_exec(command: typing.Union[str, typing.Iterable[str]], **kwargs) -> tuple[str, int]:
    """Executes the given command list"""
    if isinstance(command, str):
        commands = shlex.split(command)
    else:
        commands = [str(com) for com in command]
    try:
        logger.log(f"Executing: `{' '.join(commands)}`")
        process = subprocess.run(commands, stdout=sys.stdout, stderr=sys.stderr, check=True, **kwargs)
        # stdout, stderr = process.communicate()
        logger.debug(f'[{command!r} exited with {process.returncode}]')
        logger.debug(f'[stdout]\n{process.stdout}')
        logger.debug(f'[stderr]\n{process.stderr}')
        assert process.returncode == 0
    except (subprocess.CalledProcessError, Exception) as ex:
        raise ValueError(f"While executing process, unknown error occurred: {ex}, command: {' '.join(command)}") from ex
    else:
        return process


def test():
    """Tests translatepy"""
    logger.log("Testing `translatepy`")
    import pytest

    code = pytest.main([
        "-vvs",
        "tests/"
    ])
    if code != 0:
        raise ValueError("Tests failed for `translatepy`")


def build_website():
    """Builds the website"""
    logger.log("Building the website for `translatepy`")
    runtime = shutil.which("bun") or shutil.which("npm") or shutil.which("yarn")
    if not runtime:
        logger.error("`bun`, `npm` or `yarn` is a website build dependency and doesn't seem to be installed on your system."
                     "Please install it before proceeding with the build process.")
        raise ModuleNotFoundError("Couldn't find `bun`, `npm` or `yarn`")

    website_dir = pathlib.Path(__file__).parent / "website"
    subprocess_exec([
        runtime, "install"
    ], cwd=website_dir)
    subprocess_exec([
        runtime, "run", "build"
    ], cwd=website_dir)


def build_docs():
    """Builds the documentation"""
    logger.log("Building documentation")
    from nasse import localization as nasse_localization
    from translatepy.server.server import SERVER_DOCS_PATH
    from translatepy.server.endpoints.api import _, language

    docs_path = pathlib.Path(__file__).parent / "docs"

    logger.debug(f"Copying the main README to {docs_path / translatepy.ENGLISH.id / 'README.md'}")
    shutil.copyfile(str(pathlib.Path(__file__).parent / "README.md"),
                    str(docs_path / translatepy.ENGLISH.id / "README.md"))

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
    shutil.rmtree(SERVER_DOCS_PATH)

    logger.debug(f"Copying {docs_path} to {SERVER_DOCS_PATH}")
    shutil.copytree(str(docs_path), SERVER_DOCS_PATH)

    for language, localization in [(translatepy.ENGLISH, nasse_localization.EnglishLocalization),
                                   (translatepy.Language("french"), nasse_localization.FrenchLocalization),
                                   (translatepy.Language("japanese"), nasse_localization.JapaneseLocalization)]:

        logger.debug(f"Building server docs for `{language}`")

        # We can't just copy the result of `./docs` to `SERVER_DOCS_PATH/docs`
        # because `server.make_docs` produces different results following the
        # path given
        for docs_path in [pathlib.Path(__file__).parent / "docs" / str(language.id),
                          SERVER_DOCS_PATH / str(language.id)]:
            remove(docs_path)
            docs_path.mkdir(parents=True, exist_ok=True)

            remove(docs_path / "server")
            translatepy.server.make_docs(docs_path / "server", localization=localization)


def build_binary():
    """Builds the binaries for translatepy"""
    if sys.platform == "linux":
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
            "--static-libpython=yes", "translatepy"
        ])
    elif sys.platform == "darwin":
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
            "--static-libpython=yes", "translatepy"
        ])
    elif sys.platform == "win32":
        # logger.log("Building binaries for Windows")
        logger.error(f"We don't support building binaries for Windows yet.")
        raise ValueError("System not suitable for building binaries")
    else:
        logger.error(f"We don't support building binaries for {sys.platform} yet.")
        raise ValueError("System not suitable for building binaries")


def build():
    """Builds translatepy"""
    logger.info("`translatepy` post-build")


def release():
    """Releases translatepy"""
    logger.log("Releasing `translatepy`")


def entry(parser: argparse.ArgumentParser, arguments: typing.Optional[typing.List[str]] = None):
    """The main entrypoint for translatepy's `build` CLI"""
    subparsers = parser.add_subparsers(dest="action", description="The action to perform", required=True)

    # Language management
    language_parser = subparsers.add_parser("language", help="Manages languages in translatepy")
    language_subparsers = language_parser.add_subparsers(dest="language_action", description="the language action to perform")

    language_add_parser = language_subparsers.add_parser("add", help="Adds a language from the database")
    language_set_parser = language_subparsers.add_parser("set", help="Sets a language data")
    language_check_parser = language_subparsers.add_parser("check", help="Checks the databases")
    language_remove_parser = language_subparsers.add_parser("remove", help="Removes a language from the database")

    language_add_subparsers = language_add_parser.add_subparsers(dest="language_add_subparser", help="To add language data")
    langauge_add_code_parser = language_add_subparsers.add_parser("code")
    langauge_add_data_parser = language_add_subparsers.add_parser("data")
    langauge_add_vector_parser = language_add_subparsers.add_parser("vector")

    # Imports management
    imports_parser = subparsers.add_parser("imports", help="Manages dynamic imports in translatepy")
    imports_subparsers = imports_parser.add_subparsers(dest="imports_action", description="the dynamic imports database action to perform")

    imports_add_parser = imports_subparsers.add_parser("add", help="Adds a translator to the database")
    imports_remove_parser = imports_subparsers.add_parser("remove", help="Removes a translator from the database")

    # Library management

    def prepare_test_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the test argument parser"""
        return parser

    def prepare_website_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the website builder argument parser"""
        return parser

    def prepare_docs_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the docs builder argument parser"""
        return parser

    def prepare_binary_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the binary builder argument parser"""
        return parser

    def prepare_build_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the build argument parser"""
        return parser

    def prepare_release_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the release argument parser"""
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

    args = parser.parse_args(arguments)

    # FLOW
    # Language Management
    if args.action in ("language",):
        pass

    # Dynamic Imports Management
    if args.action in ("imports",):
        pass

    # Library Management

    if args.action in ("release", "build", "test"):
        test()

    if args.action in ("release", "build", "website"):
        build_website()

    if args.action in ("release", "build", "docs"):
        build_docs()

    if args.action in ("release", "build", "binary"):
        build_binary()

    if args.action in ("release", "build"):
        build()

    if args.action in ("release",):
        release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("translatepy build", description="translatepy helper to build the library")
    parser.add_argument("--version", "-v", action="version", version=translatepy.__version__)
    try:
        entry(parser=parser)
    except Exception:
        logger.print_exception(show_locals=("--debug" in sys.argv or "-d" in sys.argv))
