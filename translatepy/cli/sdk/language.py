"""
Language SDK

translatepy's Languages Software Development Kit
"""
import argparse
import sys

import translatepy
from translatepy import logger


def prepare_argparse(parser: argparse.ArgumentParser):
    """Prepares the given parser"""
    language_subparsers = parser.add_subparsers(dest="language_action", description="the language action to perform", required=True)

    language_add_parser = language_subparsers.add_parser("add", help="Adds a language from the database")
    language_set_parser = language_subparsers.add_parser("set", help="Sets a language data")
    language_check_parser = language_subparsers.add_parser("check", help="Checks the databases")
    language_remove_parser = language_subparsers.add_parser("remove", help="Removes a language from the database")

    language_add_subparsers = language_add_parser.add_subparsers(dest="language_add_subparser", help="To add language data", required=True)
    language_add_code_parser = language_add_subparsers.add_parser("code")
    language_add_data_parser = language_add_subparsers.add_parser("data")
    language_add_vector_parser = language_add_subparsers.add_parser("vector")


def entry(args: argparse.Namespace):
    """The main entrypoint for translatepy's `sdk` CLI"""
    # FLOW
    # Language Management


if __name__ == "__main__":
    parser = argparse.ArgumentParser("translatepy sdk language", description="translatepy's language software development kit")
    parser.add_argument("--version", "-v", action="version", version=translatepy.__version__)
    try:
        prepare_argparse(parser)
        entry(args=parser.parse_args())
    except Exception:
        logger.print_exception(show_locals=("--debug" in sys.argv or "-d" in sys.argv))
