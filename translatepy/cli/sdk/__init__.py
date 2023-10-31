"""
SDK

translatepy's Software Development Kit
"""
import argparse
import dataclasses
import datetime
import pathlib
import sys
import typing
import webbrowser

from rich.prompt import Prompt

import translatepy
from translatepy import logger
from translatepy.__info__ import __repository__
from translatepy.cli.sdk import imports, language, template
from translatepy.utils.importer import get_translator


def init(output: typing.Optional[pathlib.Path] = None, author: str = "<author>"):
    """
    Creates a new plugin directory

    This command will create a whole project folder, including repository management files,
    python project files, a license and much more.

    Parameters
    ----------
    output: pathlib.Path, default = None
        The path where the directory should be created.
        If None, it will populate the current directory.
    author: str, default = "<author>"
        The author name to use
    """
    # Here is the template base structure
    # {Name}
    # ╰──┬ .github
    #    ├────┬ dependabot.yml
    #         ├ workflows
    #         ╰────┬ codeql.yml
    #              ├ pylint.yml
    #              ├ test.yml
    #              ╰ vermin.yml
    #    ├ .gitignore
    #    ├ README.md
    #    ├ LICENSE
    #    ├ pyproject.toml
    #    ├ requirements.txt
    #    ├ poetry.lock
    #    ├ {Name}
    #    ╰──┬ README.md
    #       ├ __init__.py
    #       ╰ {name}.py

    output = output or pathlib.Path()
    output = pathlib.Path(output).resolve().absolute()
    logger.debug(f"Creating the output directory (path: {output})")
    output.mkdir(parents=True, exist_ok=True)

    # Defining the different constants
    name = output.name
    class_name = name.title()
    translator = f"{name}.{class_name}"
    year = datetime.datetime.now().year

    # Creating the `.github` directory
    logger.debug("Creating the `.github` directory")
    github_dir = (output / ".github")
    github_dir.mkdir(parents=True, exist_ok=True)
    logger.debug("Adding dependabot (ref: https://docs.github.com/en/code-security/dependabot)")
    (github_dir / "dependabot.yml").write_text(template.DEPENDABOT_TEMPLATE)

    # Populating the `.github` directory with serveral workflows
    logger.debug("Adding GitHub Actions workflows (ref: https://github.com/features/actions)")
    workdlows_dir = (github_dir / "workflows")
    workdlows_dir.mkdir(parents=True, exist_ok=True)
    (workdlows_dir / "codeql.yml").write_text(template.CODEQL_TEMPLATE)
    (workdlows_dir / "pylint.yml").write_text(template.PYLINT_TEMPLATE.format(name=name))
    (workdlows_dir / "test.yml").write_text(template.TEST_TEMPLATE.format(translator=translator))
    (workdlows_dir / "vermin.yml").write_text(template.VERMIN_TEMPLATE.format(name=name))

    # Creating repository management files
    logger.debug("Adding repository management files")
    (output / ".gitignore").write_text(template.GITIGNORE_TEMPLATE.format())
    (output / "README.md").write_text(template.README_TEMPLATE.format(name=name, class_name=class_name,
                                                                      author=author, translatepy_repo=__repository__))
    (output / "LICENSE").write_text(template.LICENSE_TEMPLATE.format(year=year, author=author))
    (output / "pyproject.toml").write_text(template.PYPROJECT_TEMPLATE.format(author=author, name=name))

    # Creating the project source directory
    logger.debug("Creating the source directory")
    src_dir = output / name
    src_dir.mkdir(parents=True, exist_ok=True)
    (src_dir / "README.md").write_text(template.SOURCE_README_TEMPLATE.format(name=name))
    (src_dir / "__init__.py").write_text(template.INIT_TEMPLATE.format(name=name, class_name=class_name, year=year, author=author))
    (src_dir / "__info__.py").write_text(template.INFO_TEMPLATE.format(name=name, year=year, author=author))
    new(src_dir / f"{name}.py")


def new(output: typing.Optional[pathlib.Path] = None):
    """
    Creates a template translator file

    Parameters
    ----------
    output: pathlib.Path, default = None
        The path for the new translator source file
    """
    # If the output is not specified,
    # generate a source file name from the directory name
    if not output:
        # A source file with the same name might already exist
        # If the user didn't supply the output name, we can't
        # overwrite the file without its permission
        counter = 1
        while (pathlib.Path() / f"translator{counter}.py").exists():
            counter += 1
        output = pathlib.Path() / f"translator{counter}.py"

    output = pathlib.Path(output).resolve().absolute()
    output.parent.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Creating the main source file (path: {output})")
    output.write_text(
        template.TRANSLATOR_TEMPLATE.format(name=output.parent.stem, class_name=output.parent.stem.title()),
        encoding="utf-8"
    )


def test(translator: typing.Union[str, typing.Type[translatepy.BaseTranslator]]):
    """
    Tests the given translator against translatepy's test suite

    Parameters
    ----------
    translator: str | translatepy.BaseTranslator
        The translator to test.
        If a string is given, the Translator class will be fetched using `translatepy.utils.importer.get_translator`.
    """
    service = translator if isinstance(translator, type) else get_translator(str(translator))

    # TODO: Add tests


def feedback(open: bool = False) -> str:
    """
    Opens the issues tracker page for the `translatepy` repository

    Parameters
    ----------
    open: bool, default = True
        If a new web browser page should be opened with the issue tracker

    Returns
    -------
    str
        The issue tracker page URL
    """
    page = f"{__repository__}/issues"
    if open:
        webbrowser.open(page)
    return page


@dataclasses.dataclass
class DebugInformation:
    """Holds a bunch of debug information"""


def debug() -> DebugInformation:
    """Displays a bunch of debug information to help diagnose problems"""
    return DebugInformation()


def prepare_argparse(parser: argparse.ArgumentParser):
    """Prepares the given parser"""
    subparsers = parser.add_subparsers(dest="sdk_action", description="The action to perform", required=True)

    # Language management
    language_parser = subparsers.add_parser("language", help="Manages languages in translatepy")
    language.prepare_argparse(language_parser)

    # Imports management
    imports_parser = subparsers.add_parser("imports", help="Manages dynamic imports in translatepy")
    imports.prepare_argparse(imports_parser)

    # `translatepy sdk init` creates a plugin directory
    init_parser = subparsers.add_parser("init", help=init.__doc__)
    init_parser.add_argument("output", help="The output directory", nargs="?")
    init_parser.add_argument("--author", help="The author name", required=False, default=None)

    # `translatepy sdk new` creates a template translator file
    new_parser = subparsers.add_parser("new", help=new.__doc__)
    new_parser.add_argument("output", help="The output filepath", nargs="?")

    # `translatepy sdk test` tests the given translator against translatepy's CI tests
    test_parser = subparsers.add_parser("test", help=test.__doc__)
    test_parser.add_argument("translator", help="A path to the translator")

    # `translatepy sdk feedback` opens the issues page for the repository
    feedback_parser = subparsers.add_parser("feedback", help=feedback.__doc__)

    # `translatepy sdk debug` displays a bunch of debug information to help diagnose problems
    debug_parser = subparsers.add_parser("debug", help=debug.__doc__)


def entry(args: argparse.Namespace):
    """The main entrypoint for translatepy's `sdk` CLI"""
    # FLOW
    # Language Management
    if args.sdk_action in ("language",):
        language.entry(args)

    # Dynamic Imports Management
    if args.sdk_action in ("imports",):
        imports.entry(args)

    if args.sdk_action in ("init",):
        if not args.author:
            author = Prompt.ask("🧑‍💻 Author name")
        else:
            author = args.author
        init(output=args.output or None, author=author)

    if args.sdk_action in ("new",):
        new(output=args.output)

    if args.sdk_action in ("test",):
        test(translator=args.translator)

    if args.sdk_action in ("feedback",):
        feedback(open=True)

    if args.sdk_action in ("debug",):
        debug()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("translatepy sdk", description="translatepy's software development kit")
    parser.add_argument("--version", "-v", action="version", version=translatepy.__version__)
    try:
        prepare_argparse(parser)
        entry(args=parser.parse_args())
    except Exception:
        logger.print_exception(show_locals=("--debug" in sys.argv or "-d" in sys.argv))
