"""
SDK

translatepy's Software Development Kit
"""
import argparse
import datetime
import pathlib
import sys
import typing
import webbrowser

from rich.prompt import Prompt

import translatepy
from translatepy import logger
from translatepy.__info__ import __repository__
from translatepy.utils.importer import get_translator
from translatepy.cli.sdk import imports, language, template


def init(output: typing.Optional[pathlib.Path] = None, author: str = "<author>"):
    """
    Creates a new plugin directory

    Here is the template base structure
    {Name}
    ╰──┬ .github
       ├────┬ dependabot.yml
            ├ workflows
            ╰────┬ codeql.yml
                 ├ pylint.yml
                 ├ test.yml
                 ╰ vermin.yml
       ├ .gitignore
       ├ README.md
       ├ LICENSE
       ├ pyproject.toml
       ├ requirements.txt
       ├ poetry.lock
       ├ {Name}
       ╰──┬ README.md
          ├ __init__.py
          ╰ {name}.py
    """
    output = output or pathlib.Path()
    output = pathlib.Path(output).resolve().absolute()
    output.mkdir(parents=True, exist_ok=True)

    name = output.name
    class_name = name.title()
    translator = f"{name}.{class_name}"
    year = datetime.datetime.now().year

    github_dir = (output / ".github")
    github_dir.mkdir(parents=True, exist_ok=True)
    (github_dir / "dependabot.yml").write_text(template.DEPENDABOT_TEMPLATE)

    workdlows_dir = (github_dir / "workflows")
    workdlows_dir.mkdir(parents=True, exist_ok=True)
    (workdlows_dir / "codeql.yml").write_text(template.CODEQL_TEMPLATE)
    (workdlows_dir / "pylint.yml").write_text(template.PYLINT_TEMPLATE.format(name=name))
    (workdlows_dir / "test.yml").write_text(template.TEST_TEMPLATE.format(translator=translator))
    (workdlows_dir / "vermin.yml").write_text(template.VERMIN_TEMPLATE.format(name=name))

    (output / ".gitignore").write_text(template.GITIGNORE_TEMPLATE.format())
    (output / "README.md").write_text(template.README_TEMPLATE.format(name=name, class_name=class_name, author=author, translatepy_repo=__repository__))
    (output / "LICENSE").write_text(template.LICENSE_TEMPLATE.format(year=year, author=author))
    (output / "pyproject.toml").write_text(template.PYPROJECT_TEMPLATE.format(author=author, name=name))

    src_dir = output / name
    src_dir.mkdir(parents=True, exist_ok=True)
    (src_dir / "README.md").write_text(template.SOURCE_README_TEMPLATE.format(name=name))
    (src_dir / "__init__.py").write_text(template.INIT_TEMPLATE.format(name=name, class_name=class_name, year=year, author=author))
    (src_dir / "__info__.py").write_text(template.INFO_TEMPLATE.format(name=name, year=year, author=author))
    new(src_dir / f"{name}.py")


def new(output: typing.Optional[pathlib.Path] = None):
    """Creates a template translator file"""
    if not output:
        counter = 1
        while (pathlib.Path() / f"translator{counter}.py").exists():
            counter += 1
        output = pathlib.Path() / f"translator{counter}.py"
    output = pathlib.Path(output).resolve().absolute()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        template.TRANSLATOR_TEMPLATE.format(name=output.parent.stem, class_name=output.parent.stem.title())
    )


def test(translator: str):
    """Tests the given translator against translatepy's test suite"""
    service = get_translator(translator)
    # Run tests on `service`


def feedback():
    """Opens the issues tracker page for the `translatepy` repository"""
    webbrowser.open(f"{__repository__}/issues")


def debug():
    """Displays a bunch of debug information to help diagnose problems"""


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
        feedback()

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
