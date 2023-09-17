"""
SDK

translatepy's Software Development Kit
"""
import argparse
import sys

import translatepy
from translatepy import logger


def prepare_argparse(parser: argparse.ArgumentParser):
    """Prepares the given parser"""
    subparsers = parser.add_subparsers(dest="sdk_action", description="The action to perform", required=True)

    # Language management
    language_parser = subparsers.add_parser("language", help="Manages languages in translatepy")
    language_subparsers = language_parser.add_subparsers(dest="language_action", description="the language action to perform", required=True)

    language_add_parser = language_subparsers.add_parser("add", help="Adds a language from the database")
    language_set_parser = language_subparsers.add_parser("set", help="Sets a language data")
    language_check_parser = language_subparsers.add_parser("check", help="Checks the databases")
    language_remove_parser = language_subparsers.add_parser("remove", help="Removes a language from the database")

    language_add_subparsers = language_add_parser.add_subparsers(dest="language_add_subparser", help="To add language data", required=True)
    langauge_add_code_parser = language_add_subparsers.add_parser("code")
    langauge_add_data_parser = language_add_subparsers.add_parser("data")
    langauge_add_vector_parser = language_add_subparsers.add_parser("vector")

    # Imports management
    imports_parser = subparsers.add_parser("imports", help="Manages dynamic imports in translatepy")
    imports_subparsers = imports_parser.add_subparsers(dest="imports_action", description="the dynamic imports database action to perform", required=True)

    imports_add_parser = imports_subparsers.add_parser("add", help="Adds a translator to the database")
    imports_remove_parser = imports_subparsers.add_parser("remove", help="Removes a translator from the database")

    # `translatepy sdk init` creates a plugin directory
    # `translatepy sdk new` creates a template translator file
    # `translatepy sdk test` tests the given translator against translatepy's CI tests


def entry(args: argparse.Namespace):
    """The main entrypoint for translatepy's `sdk` CLI"""
    # FLOW
    # Language Management
    if args.sdk_action in ("language",):
        pass

    # Dynamic Imports Management
    if args.sdk_action in ("imports",):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser("translatepy sdk", description="translatepy's software development kit")
    parser.add_argument("--version", "-v", action="version", version=translatepy.__version__)
    try:
        prepare_argparse(parser)
        entry(args=parser.parse_args())
    except Exception:
        logger.print_exception(show_locals=("--debug" in sys.argv or "-d" in sys.argv))
