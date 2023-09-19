"""
Imports SDK

translatepy's Imports Software Development Kit
"""
import argparse
import sys
import typing
import dataclasses
import json

import cain

import translatepy
from translatepy import logger
from translatepy.__info__ import __repository__
from translatepy.utils import vectorize, importer


def add(name: str, path: str, translate: bool = False, forceload: bool = False):
    """Adds a translator to the database"""
    name = str(name)

    importer.get_translator_from_path(path, forceload=forceload)

    names = [name]
    if translate:
        for lang in []:
            try:
                result = translatepy.translate(name, lang)
                names.append(result.translation)
            except Exception:
                pass
    for name in names:
        importer.IMPORTER_VECTORS.append(
            vectorize.vectorize(path, name)
        )
    with (importer.IMPORTER_DATA_DIR / "translators").open("wb") as f:
        cain.dump(importer.IMPORTER_VECTORS, f, typing.List[vectorize.Vector])


def remove(name: str):
    """Removes a translator from the database"""
    vectors = [vector for vector in importer.IMPORTER_VECTORS if vector.string != name]
    with (importer.IMPORTER_DATA_DIR / "translators").open("wb") as f:
        cain.dump(vectors, f, typing.List[vectorize.Vector])


def search(query: str, limit: int = 10):
    """Searches for the given `query` in the database"""
    results = sorted(vectorize.search(query, importer.IMPORTER_VECTORS), key=lambda element: element.similarity, reverse=True)
    print(json.dumps([{
        "similarity": vector.similarity,
        "vector": vector.vector._cain_value
    } for vector in results[:limit]], ensure_ascii=False, indent=4))


def available():
    """Displays the available translators"""
    print(json.dumps(list(set(vector.id for vector in importer.IMPORTER_VECTORS)), ensure_ascii=False, indent=4))


def prepare_argparse(parser: argparse.ArgumentParser):
    """Prepares the given parser"""
    imports_subparsers = parser.add_subparsers(dest="imports_action", description="the dynamic imports database action to perform", required=True)

    imports_add_parser = imports_subparsers.add_parser("add", help=add.__doc__)
    imports_add_parser.add_argument("name", help="The translator name")
    imports_add_parser.add_argument("--path", "-p", help="The dot path to the translator (ex: `translatepy.translators.google.GoogleTranslate`)")
    imports_add_parser.add_argument("--translate", "-t", action="store_true", help="Automatically translates the name")
    imports_add_parser.add_argument("--forceload", action="store_true", help="Enables pydoc's `forceload` while searching for the translator")

    imports_remove_parser = imports_subparsers.add_parser("remove", help=remove.__doc__)
    imports_remove_parser.add_argument("name", help="The translator name")

    imports_search_parser = imports_subparsers.add_parser("search", help=search.__doc__)
    imports_search_parser.add_argument("query", help="The search query")
    imports_search_parser.add_argument("--limit", help="The maximum number of results", type=int, default=10)

    imports_available_parser = imports_subparsers.add_parser("available", help=available.__doc__)


def entry(args: argparse.Namespace):
    """The main entrypoint for translatepy's `sdk` CLI"""
    # FLOW
    # Imports Management
    if args.imports_action in ("add",):
        add(name=args.name, path=args.path, translate=args.translate, forceload=args.forceload)

    if args.imports_action in ("remove",):
        remove(name=args.name)

    if args.imports_action in ("search",):
        search(query=args.query, limit=args.limit)

    if args.imports_action in ("available",):
        available()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("translatepy sdk imports", description="translatepy's imports software development kit")
    parser.add_argument("--version", "-v", action="version", version=translatepy.__version__)
    try:
        prepare_argparse(parser)
        entry(args=parser.parse_args())
    except Exception:
        logger.print_exception(show_locals=("--debug" in sys.argv or "-d" in sys.argv))
