"""
Imports SDK

translatepy's Imports Software Development Kit
"""
import argparse
import sys
import typing

import cain
from nasse.exceptions import NasseException
from nasse.utils.json import encoder, minified_encoder
from rich.progress import Progress

import translatepy
from translatepy import logger
from translatepy.__info__ import __repository__
from translatepy.language import COMMON_LANGUAGES
from translatepy.utils import importer, vectorize


def json_encode(args: argparse.Namespace, work: typing.Callable, **kwargs):
    """Enforces the JSON encoding"""
    json_encoder = minified_encoder if args.minified else encoder

    def prepare_error(err: Exception) -> dict:
        """Prepare an error to return to the user"""
        if isinstance(err, NasseException):
            return {
                "success": False,
                "exception": err.EXCEPTION_NAME,
                "message": err.MESSAGE,
                "code": err.STATUS_CODE
            }
        return {
            "success": False,
            "exception": err.__class__.__name__,
            "message": str(err),
            "code": -1
        }
    try:
        print(json_encoder.encode(work(**kwargs)))
        return 0
    except Exception as err:
        error_data = prepare_error(err)
        print(json_encoder.encode(error_data))
        return error_data["code"]


def add(name: str, path: str, translate: bool = False, forceload: bool = False):
    """Adds a translator to the database"""
    name = str(name)

    # Verify that the path exists
    importer.translator_from_path(path, forceload=forceload)

    names = [name]
    if translate:
        logger.info(f"Translating `{name}`")
        with Progress(console=logger._rich_console, transient=True) as progress:
            main_task = progress.add_task(f"Translating `{name}`", total=len(COMMON_LANGUAGES))
            for lang in COMMON_LANGUAGES:
                progress.update(main_task, description=f"Translating `{name}` to `{lang}`")
                try:
                    logger.debug(f"Translating `{name}` in `{lang}`")
                    result = translatepy.translate(name, lang)
                    names.append(result.translation)
                    logger.debug(f"Translation result: {result}")
                except Exception as err:
                    logger.warn(f"An error occured while translating `{name}` to `{lang}`")
                    logger.warn(err)

                progress.advance(main_task)

    logger.debug("Vectorizing the new names")
    for name in names:
        importer.IMPORTER_VECTORS.append(
            vectorize.vectorize(path, name)
        )

    logger.info("Dumping the vectors to the translators DB")
    with (importer.IMPORTER_DATA_FILE).open("wb") as f:
        cain.dump(importer.IMPORTER_VECTORS, f, typing.List[vectorize.Vector])


def remove(name: str, all: bool = False):
    """Removes a translator name variant from the database"""
    if all:
        vectors = [vector for vector in importer.IMPORTER_VECTORS if vector.id != name]
    else:
        name = vectorize.string_preprocessing(name)
        vectors = [vector for vector in importer.IMPORTER_VECTORS if vector.string != name]
    with (importer.IMPORTER_DATA_FILE).open("wb") as f:
        cain.dump(vectors, f, typing.List[vectorize.Vector])


def variants(translator: str):
    """Returns all of the name variants available in the database for the given translator ID"""
    vectors = [vector for vector in importer.IMPORTER_VECTORS if vector.id == translator]
    return [vector.string for vector in vectors]


def search(query: str, limit: int = 10):
    """Searches for the given `query` in the database"""
    results = sorted(vectorize.search(query, importer.IMPORTER_VECTORS), key=lambda element: element.similarity, reverse=True)
    if limit >= 0:
        return results[:limit]
    return results


def available():
    """Displays the available translators"""
    return {vector.id for vector in importer.IMPORTER_VECTORS}


def prepare_argparse(parser: argparse.ArgumentParser):
    """Prepares the given parser"""
    imports_subparsers = parser.add_subparsers(dest="imports_action", description="the dynamic imports database action to perform", required=True)

    def prepare_json_parser(parser: argparse.ArgumentParser):
        parser.add_argument("--minified", "--minify", "--mini", action="store_true", help="To minify the resulting JSON")

    imports_add_parser = imports_subparsers.add_parser("add", help=add.__doc__)
    imports_add_parser.add_argument("name", help="The translator name")
    imports_add_parser.add_argument("--path", "-p", help="The dot path to the translator (ex: `translatepy.translators.google.GoogleTranslate`)")
    imports_add_parser.add_argument("--translate", "-t", action="store_true", help="Automatically translates the name")
    imports_add_parser.add_argument("--forceload", action="store_true", help="Enables pydoc's `forceload` while searching for the translator")

    imports_remove_parser = imports_subparsers.add_parser("remove", help=remove.__doc__)
    imports_remove_parser.add_argument("name", help="The translator name variant or id if `--all` is set")
    imports_remove_parser.add_argument("--all", action="store_true", help="Treats `name` as the translator ID and removes every variants associated with the translator")

    imports_variants_parser = imports_subparsers.add_parser("variants", help=variants.__doc__)
    prepare_json_parser(imports_variants_parser)
    imports_variants_parser.add_argument("id", help="The translator ID")

    imports_search_parser = imports_subparsers.add_parser("search", help=search.__doc__)
    prepare_json_parser(imports_search_parser)
    imports_search_parser.add_argument("query", help="The search query")
    imports_search_parser.add_argument("--limit", help="The maximum number of results", type=int, default=10)

    imports_available_parser = imports_subparsers.add_parser("available", help=available.__doc__)
    prepare_json_parser(imports_available_parser)


def entry(args: argparse.Namespace):
    """The main entrypoint for translatepy's `sdk` CLI"""
    # FLOW
    # Imports Management
    if args.imports_action in ("add",):
        add(name=args.name, path=args.path, translate=args.translate, forceload=args.forceload)

    if args.imports_action in ("remove",):
        remove(name=args.name, all=args.all)

    if args.imports_action in ("variants",):
        json_encode(args, variants, translator=args.id)

    if args.imports_action in ("search",):
        json_encode(args, search, query=args.query, limit=args.limit)

    if args.imports_action in ("available",):
        json_encode(args, available)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("translatepy sdk imports", description="translatepy's imports software development kit")
    parser.add_argument("--version", "-v", action="version", version=translatepy.__version__)
    try:
        prepare_argparse(parser)
        entry(args=parser.parse_args())
    except Exception:
        logger.print_exception(show_locals=("--debug" in sys.argv or "-d" in sys.argv))
