"""
build.py

Compiles everything down
"""
import argparse
import translatepy


def test():
    """Tests translatepy"""


def build_website():
    """Builds the website"""


def build_docs():
    """Builds the server documentation"""


def build_binary():
    """Builds the binaries for translatepy"""


def build():
    """Builds translatepy"""


def release():
    """Releases translatepy"""


def entry():
    """The main entrypoint for translatepy's `build` CLI"""
    parser = argparse.ArgumentParser("translatepy build", description="translatepy helper to build the library")
    parser.add_argument("--version", "-v", action="version", version=translatepy.__version__)
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

    args = parser.parse_args()

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
    entry()
