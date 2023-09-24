"""
Language SDK

translatepy's Languages Software Development Kit
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
from translatepy.exceptions import UnknownLanguage
from translatepy.language import COMMON_LANGUAGES, TRANSLATEPY_LANGUAGE_FULL
from translatepy.language import DATA as LANGUAGE_DATA
from translatepy.language import (LANGUAGE_DATA_DIR, NULLABLE_ATTRIBUTES,
                                  Foreign, Language, LanguageExtra)
from translatepy.utils import vectorize


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


def add(name: str, code: str, alpha3: typing.Optional[str] = None,
        translate: bool = False, **kwargs):
    """Adds a translator to the database"""
    name = str(name)

    # Verify that the code exists, or add it
    code_id = LANGUAGE_DATA["codes"].get(code, None)
    if not code_id:
        LANGUAGE_DATA["codes"][code] = code
        code_id = code

    # Checking the vectors DB
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
        LANGUAGE_DATA["vectors"].append(
            vectorize.vectorize(code_id, name)
        )

    # Checking the data DB
    data = LANGUAGE_DATA["data"].get(code)
    data = data or Language({
        "id": code_id,
        "name": name,
        "alpha3": alpha3 or code,
        **{key: None for key in NULLABLE_ATTRIBUTES}
    })
    for attr in NULLABLE_ATTRIBUTES:
        if not data[attr]:
            data._cain_value[attr] = kwargs.get(attr, None)

    if data.foreign:
        for lang, result in data.foreign.items():
            if not result:
                result = kwargs.get("foreign", {}).get(lang, data.name)
                data.foreign[lang] = result  # default to the english name

    LANGUAGE_DATA["data"][code] = data

    # Creating backups
    with (LANGUAGE_DATA_DIR / "codes.cain").open("rb") as f:
        backup_codes = f.read()
    with (LANGUAGE_DATA_DIR / "vectors.cain").open("rb") as f:
        backup_vectors = f.read()
    with (LANGUAGE_DATA_DIR / "data.cain").open("rb") as f:
        backup_data = f.read()
    with (LANGUAGE_DATA_DIR / "data_full.cain").open("rb") as f:
        backup_data_full = f.read()

    # Writing out
    try:
        logger.info("Dumping the codes to the languages DB")
        with (LANGUAGE_DATA_DIR / "codes.cain").open("wb") as f:
            cain.dump([(code, result) for code, result in LANGUAGE_DATA["codes"].items()], f, typing.List[typing.Tuple[str, str]])

        logger.info("Dumping the vectors to the languages DB")
        with (LANGUAGE_DATA_DIR / "vectors.cain").open("wb") as f:
            cain.dump(LANGUAGE_DATA["vectors"], f, typing.List[vectorize.Vector])

        logger.info("Dumping the data to the languages DB")
        with (LANGUAGE_DATA_DIR / ("data_full.cain" if TRANSLATEPY_LANGUAGE_FULL
                                   else "data.cain")).open("wb") as f:
            cain.dump(LANGUAGE_DATA["data"].values(), f, typing.List[Language])
        if not TRANSLATEPY_LANGUAGE_FULL:
            logger.warning("The full range language DB is not affected. Please rerun the same command with `--full`.")
        else:
            logger.warning("The limited range language DB is not affected. Please rerun the same command without `--full`.")
    except Exception as err:
        logger.error("An error occured while writing out the data to the languages DB")
        if logger.config.debug:
            logger.print_exception(show_locals=True)
        else:
            logger.error(err)
        logger.warn("Reverting to previous state")
        with (LANGUAGE_DATA_DIR / "codes.cain").open("wb") as f:
            f.write(backup_codes)
        with (LANGUAGE_DATA_DIR / "vectors.cain").open("wb") as f:
            f.write(backup_vectors)
        with (LANGUAGE_DATA_DIR / "data.cain").open("wb") as f:
            f.write(backup_data)
        with (LANGUAGE_DATA_DIR / "data_full.cain").open("wb") as f:
            f.write(backup_data_full)


def set(id: str,
        name: typing.Optional[str] = None,
        alpha3: typing.Optional[str] = None,
        **kwargs):
    """Sets the language data"""
    data = LANGUAGE_DATA["data"][id]

    if name:
        data._cain_value["name"] = name
    if alpha3:
        data._cain_value["alpha3"] = alpha3

    for attr in NULLABLE_ATTRIBUTES:
        if not data[attr]:
            data._cain_value[attr] = kwargs.get(attr, None)

    if data.foreign:
        for lang, result in data.foreign.items():
            if not result:
                result = kwargs.get("foreign", {}).get(lang, data.name)
                data.foreign[lang] = result  # default to the english name

    LANGUAGE_DATA["data"][id] = data

    logger.info("Dumping the data to the languages DB")
    with (LANGUAGE_DATA_DIR / ("data_full.cain" if TRANSLATEPY_LANGUAGE_FULL
                               else "data.cain")).open("wb") as f:
        cain.dump(LANGUAGE_DATA["data"].values(), f, typing.List[Language])

    if not TRANSLATEPY_LANGUAGE_FULL:
        logger.warning("The full range language DB is not affected. Please rerun the same command with `--full`.")
    else:
        logger.warning("The limited range language DB is not affected. Please rerun the same command without `--full`.")


def remove(name: str, all: bool = False):
    """Removes a translator name variant from the database"""
    if all:
        codes = {code: result for code, result in LANGUAGE_DATA["codes"].items() if result != name}
        vectors = [vector for vector in LANGUAGE_DATA["vectors"] if vector.id != name]
        data = {code: result for code, result in LANGUAGE_DATA["data"] if code != name}

        # Creating backups
        with (LANGUAGE_DATA_DIR / "codes.cain").open("rb") as f:
            backup_codes = f.read()
        with (LANGUAGE_DATA_DIR / "vectors.cain").open("rb") as f:
            backup_vectors = f.read()
        with (LANGUAGE_DATA_DIR / "data.cain").open("rb") as f:
            backup_data = f.read()
        with (LANGUAGE_DATA_DIR / "data_full.cain").open("rb") as f:
            backup_data_full = f.read()

        # Writing out
        try:
            logger.info("Dumping the codes to the languages DB")
            with (LANGUAGE_DATA_DIR / "codes.cain").open("wb") as f:
                cain.dump([(code, result) for code, result in codes.items()], f, typing.List[typing.Tuple[str, str]])

            logger.info("Dumping the vectors to the languages DB")
            with (LANGUAGE_DATA_DIR / "vectors.cain").open("wb") as f:
                cain.dump(vectors, f, typing.List[vectorize.Vector])

            logger.info("Dumping the data to the languages DB")
            with (LANGUAGE_DATA_DIR / ("data_full.cain" if TRANSLATEPY_LANGUAGE_FULL
                                       else "data.cain")).open("wb") as f:
                cain.dump(data.values(), f, typing.List[Language])

            if not TRANSLATEPY_LANGUAGE_FULL:
                logger.warning("The full range language DB is not affected. Please rerun the same command with `--full`.")
            else:
                logger.warning("The limited range language DB is not affected. Please rerun the same command without `--full`.")

        except Exception as err:
            logger.error("An error occured while writing out the data to the languages DB")
            logger.error(err)
            logger.warn("Reverting to previous state")
            with (LANGUAGE_DATA_DIR / "codes.cain").open("wb") as f:
                f.write(backup_codes)
            with (LANGUAGE_DATA_DIR / "vectors.cain").open("wb") as f:
                f.write(backup_vectors)
            with (LANGUAGE_DATA_DIR / "data.cain").open("wb") as f:
                f.write(backup_data)
            with (LANGUAGE_DATA_DIR / "data_full.cain").open("wb") as f:
                f.write(backup_data_full)

    else:
        name = vectorize.string_preprocessing(name)
        vectors = [vector for vector in LANGUAGE_DATA["vectors"] if vector.string != name]
        with (LANGUAGE_DATA_DIR / "vectors.cain").open("wb") as f:
            cain.dump(vectors, f, typing.List[vectorize.Vector])


def variants(language: str):
    """Returns all of the name variants available in the database for the given translator ID"""
    lang = Language(language)
    vectors = [vector for vector in LANGUAGE_DATA["vectors"] if vector.id == lang.id]
    return [vector.string for vector in vectors]


def search(query: str, limit: int = 10):
    """Searches for the given `query` in the database"""
    results = Language.search(query)
    if limit >= 0:
        return results[:limit]
    return results


def info(language: str):
    """Displays information about the given language"""
    return Language(language)


def available():
    """Displays the available translators"""
    return set(vector.id for vector in LANGUAGE_DATA["vectors"])


def prepare_argparse(parser: argparse.ArgumentParser):
    """Prepares the given parser"""
    language_subparsers = parser.add_subparsers(dest="language_action", description="the language action to perform", required=True)

    def prepare_json_parser(parser: argparse.ArgumentParser):
        parser.add_argument("--minified", "--mini", action="store_true", help="To minify the resulting JSON")

    def prepare_set_parser(parser: argparse.ArgumentParser):
        parser.add_argument("--alpha3", help="The ISO 639-3 (Alpha-3) code", required=False, default=None)
        parser.add_argument("--alpha2", help="The ISO 639-1 (Alpha-2) code", required=False, default=None)
        parser.add_argument("--alpha3b", help="The ISO 639-2B (Alpha-3) code", required=False, default=None)
        parser.add_argument("--alpha3t", help="The ISO 639-2T (Alpha-3) code", required=False, default=None)

        parser.add_argument("--scope", help="Language scope. Needs `--type`.", required=False, default=None, choices=["individual", "macrolanguage", "special"])
        parser.add_argument("--type", help="Language type. Needs `--scope`.", required=False, default=None, choices=["ancient", "constructed", "extinct",
                                                                                                                     "historical", "living", "special"])

        parser.add_argument("--foreign", help="Foreign name for the language. Can be used multiple times. Should be formatted as <lang>:<result>. Example: `--foreign=french:Japonais`", action="append")

    language_add_parser = language_subparsers.add_parser("add", help=add.__doc__)
    language_add_parser.add_argument("name", help="The language name")
    language_add_parser.add_argument("--code", "-c", help="Its language code")
    language_add_parser.add_argument("--translate", "-t", action="store_true", help="Automatically translates the name")
    prepare_set_parser(language_add_parser)

    language_set_parser = language_subparsers.add_parser("set", help=set.__doc__)
    language_set_parser.add_argument("id", help="The language ID")
    language_set_parser.add_argument("--name", help="The language name")
    prepare_set_parser(language_set_parser)

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
    def check_extra():
        """Checks for extra data inputs"""
        if args.scope or args.type:
            if not args.scope:
                raise ValueError("`--scope` is required when using `--type`")
            if not args.type:
                raise ValueError("`--type` is required when using `--scope`")
            return LanguageExtra({
                "scope": args.scope,
                "type": args.type
            })
        return None

    def check_foreign():
        """Checks for foreign inputs"""
        results = {vectorize.string_preprocessing(lang.name): None for lang in COMMON_LANGUAGES if lang.id != "eng"}
        if not args.foreign:
            return results

        for element in args.foreign:
            lang, _, result = element.partition(":")
            language = Language(lang)
            lang = vectorize.string_preprocessing(language.name)
            if lang not in results:
                raise ValueError(f"The given language `{lang}` doesn't seem to be supported for foreign translations")
            results[lang] = result
        return results

    if args.language_action in ("add",):
        add(name=args.name, code=args.code, alpha3=args.alpha3, translate=args.translate,
            alpha2=args.alpha2,
            alpha3b=args.alpha3b,
            alpha3t=args.alpha3t,
            extra=check_extra(),
            foreign=check_foreign())

    if args.language_action in ("set",):
        set(id=args.id, name=args.name, alpha3=args.alpha3,
            alpha2=args.alpha2,
            alpha3b=args.alpha3b,
            alpha3t=args.alpha3t,
            extra=check_extra(),
            foreign=check_foreign())

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
