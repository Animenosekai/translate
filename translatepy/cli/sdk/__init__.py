"""
SDK

translatepy's Software Development Kit
"""
import argparse
import pathlib
import sys
import typing
import webbrowser

import translatepy
from translatepy import logger
from translatepy.cli.sdk import language, imports
from translatepy.__info__ import __repository__


def init(output: typing.Optional[pathlib.Path] = None):
    """Creates a new plugin directory"""


def new(output: typing.Optional[pathlib.Path] = None):
    """Creates a template translator file"""


def test():
    """Tests the given translator against translatepy's test suite"""


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

    # `translatepy sdk new` creates a template translator file
    new_parser = subparsers.add_parser("new", help=new.__doc__)

    # `translatepy sdk test` tests the given translator against translatepy's CI tests
    test_parser = subparsers.add_parser("test", help=test.__doc__)

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
        init()

    if args.sdk_action in ("new",):
        new()

    if args.sdk_action in ("test",):
        test()

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
