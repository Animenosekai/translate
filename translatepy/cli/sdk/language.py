"""
Language SDK

translatepy's Languages Software Development Kit
"""
import argparse
import sys
import typing

import cain
from nasse.exceptions import NasseException
from nasse.utils.json import NasseJSONEncoder, encoder, minified_encoder
from rich.progress import Progress

import translatepy
from translatepy import logger
from translatepy.__info__ import __repository__
from translatepy.exceptions import UnknownLanguage
from translatepy.language import COMMON_LANGUAGES
from translatepy.language import DATA as LANGUAGE_DATA
from translatepy.language import Language
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
        work(json_encoder=json_encoder, **kwargs)
        return 0
    except UnknownLanguage as err:
        error_data = {
            **prepare_error(err),
            "guessed_language": err.guessed_language,
            "similarity": err.similarity,
        }
        print(json_encoder.encode(error_data))
        return error_data["code"]
    except Exception as err:
        error_data = prepare_error(err)
        print(json_encoder.encode(error_data))
        return error_data["code"]


def add(name: str, code: str, translate: bool = False):
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
        vectors = [vector for vector in LANGUAGE_DATA["vectors"] if vector.id != name]
    else:
        name = vectorize.string_preprocessing(name)
        vectors = [vector for vector in LANGUAGE_DATA["vectors"] if vector.string != name]
    with (importer.IMPORTER_DATA_FILE).open("wb") as f:
        cain.dump(vectors, f, typing.List[vectorize.Vector])


def variants(json_encoder: NasseJSONEncoder, language: str):
    """Returns all of the name variants available in the database for the given translator ID"""
    lang = Language(language)
    vectors = [vector for vector in LANGUAGE_DATA["vectors"] if vector.id == lang.id]
    print(json_encoder.encode([vector.string for vector in vectors]))


def search(json_encoder: NasseJSONEncoder, query: str, limit: int = 10):
    """Searches for the given `query` in the database"""
    results = Language.search(query)
    print(json_encoder.encode(results[:limit]))
    # print(json.dumps([{
    #     "similarity": vector.similarity,
    #     "vector": vector.vector._cain_value
    # } for vector in results[:limit]], ensure_ascii=False, indent=4))


def info(json_encoder: NasseJSONEncoder, language: str):
    """Displays information about the given language"""
    lang = Language(language)
    print(json_encoder.encode(lang))


def available(json_encoder: NasseJSONEncoder):
    """Displays the available translators"""
    print(json_encoder.encode(set(vector.id for vector in LANGUAGE_DATA["vectors"])))
    # print(json.dumps(list(set(vector.id for vector in LANGUAGE_DATA["vectors"])), ensure_ascii=False, indent=4))


def prepare_argparse(parser: argparse.ArgumentParser):
    """Prepares the given parser"""
    language_subparsers = parser.add_subparsers(dest="language_action", description="the language action to perform", required=True)

    def prepare_json_parser(parser: argparse.ArgumentParser):
        parser.add_argument("--minified", "--mini", action="store_true", help="To minify the resulting JSON")

    language_add_parser = language_subparsers.add_parser("add", help=add.__doc__)
    language_add_parser.add_argument("name", help="The language name")
    language_add_parser.add_argument("--code", "-c", help="Its language code")
    language_add_parser.add_argument("--translate", "-t", action="store_true", help="Automatically translates the name")

    language_remove_parser = language_subparsers.add_parser("remove", help=remove.__doc__)
    language_remove_parser.add_argument("name", help="The language name variant or id if `--all` is set")
    language_remove_parser.add_argument("--all", action="store_true", help="Treats `name` as a language code and removes every variants associated with the language")

    language_variants_parser = language_subparsers.add_parser("variants", help=variants.__doc__)
    prepare_json_parser(language_variants_parser)
    language_variants_parser.add_argument("id", help="The language ID")

    language_search_parser = language_subparsers.add_parser("search", help=search.__doc__)
    prepare_json_parser(language_search_parser)
    language_search_parser.add_argument("query", help="The search query")
    language_search_parser.add_argument("--limit", help="The maximum number of results", type=int, default=10)

    language_info_parser = language_subparsers.add_parser("info", help=info.__doc__)
    prepare_json_parser(language_info_parser)
    language_info_parser.add_argument("language", help="The language to get informations for")

    language_available_parser = language_subparsers.add_parser("available", help=available.__doc__)
    prepare_json_parser(language_available_parser)


def entry(args: argparse.Namespace):
    """The main entrypoint for translatepy's `sdk` CLI"""
    # FLOW
    # Language Management
    if args.language_action in ("add",):
        add(name=args.name, code=args.code, translate=args.translate)

    if args.language_action in ("remove",):
        remove(name=args.name, all=args.all)

    if args.language_action in ("variants",):
        json_encode(args, variants, language=args.id)

    if args.language_action in ("search",):
        json_encode(args, search, query=args.query, limit=args.limit)

    if args.language_action in ("info",):
        json_encode(args, info, language=args.language)

    if args.language_action in ("available",):
        json_encode(args, available)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("translatepy sdk language", description="translatepy's language software development kit")
    parser.add_argument("--version", "-v", action="version", version=translatepy.__version__)
    try:
        prepare_argparse(parser)
        entry(args=parser.parse_args())
    except Exception:
        logger.print_exception(show_locals=("--debug" in sys.argv or "-d" in sys.argv))
