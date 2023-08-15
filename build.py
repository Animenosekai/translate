"""
build.py

Compiles everything down
"""
import subprocess
import typing
import argparse
import translatepy


def build_website():
    pass


def build_docs():
    pass


def entry():
    parser = argparse.ArgumentParser("translatepy build", description="translatepy helper to build")
    parser.add_argument("--version", "-v", action="version", version=translatepy.__version__)
    subparsers = parser.add_subparsers(dest="action", description="The action to perform", required=True)
    all_parser = subparsers.add_parser("all", help="Performs all actions")

    def prepare_website_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the website argument parser"""
        return parser

    def prepare_docs_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """Prepares the docs argument parser"""
        return parser

    prepare_website_parser(all_parser)
    prepare_website_parser(all_parser)

    website_parser = prepare_website_parser(subparsers.add_parser("website", help=build_website.__doc__))
    docs_parser = prepare_docs_parser(subparsers.add_parser("docs", help=build_docs.__doc__))

    args = parser.parse_args()

    if args.action in ("all", "website"):
        pass

    if args.action in ("all", "docs"):
        pass

    build_website()
    build_docs()


if __name__ == "__main__":
    entry()
