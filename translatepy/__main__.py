import argparse
from json import dumps
from traceback import print_exc

import inquirer

import translatepy
from translatepy.exceptions import UnknownLanguage, VersionNotSupported

INPUT_PREFIX = "(\033[90mtranslatepy ~ \033[0m{action}) > "

NO_ACTION = """\
usage: translatepy [-h] [--version] {translate,transliterate,spellcheck,language,shell,server} ...
translatepy: error: the following arguments are required: action"""

actions = [
    inquirer.List(
        name='action',
        message="What do you want to do?",
        choices=['Translate', 'Transliterate', 'Spellcheck', 'Language', 'Example', 'Quit'],
        carousel=True
    )
]


def main():
    # Create the parser
    parser = argparse.ArgumentParser(prog='translatepy', description='Translate, transliterate, get the language of texts in no time with the help of multiple APIs!')

    parser.add_argument('--version', '-v', action='version', version=translatepy.__version__)
    parser.add_argument("--translators", action="store", type=str, help="List of translators to use. Each translator name should be comma-separated.", required=False, default=None)

    # subparser = parser.add_subparsers(help='Actions', dest="action", required=True)
    subparser = parser.add_subparsers(help='Actions', dest="action")

    parser_translate = subparser.add_parser('translate', help='Translates the given text to the given language')
    parser_translate.add_argument('--text', '-t', action='store', type=str, required=True, help='text to translate')
    parser_translate.add_argument('--dest-lang', '-d', action='store', type=str, required=True, help='destination language')
    parser_translate.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_transliterate = subparser.add_parser('transliterate', help='Transliterates the given text')
    parser_transliterate.add_argument('--text', '-t', action='store', type=str, required=True, help='text to transliterate')
    parser_transliterate.add_argument('--dest-lang', '-d', action='store', type=str, default="en", help='destination language')
    parser_transliterate.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_spellcheck = subparser.add_parser('spellcheck', help='Checks the spelling of the given text')
    parser_spellcheck.add_argument('--text', '-t', action='store', type=str, required=True, help='text to spellcheck')
    parser_spellcheck.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_language = subparser.add_parser('language', help='Checks the language of the given text')
    parser_language.add_argument('--text', '-t', action='store', type=str, required=True, help='text to check the language')

    parser_shell = subparser.add_parser('shell', help="Opens translatepy's interactive mode")
    parser_shell.add_argument('--dest-lang', '-d', action='store', default=None, type=str, help='destination language')
    parser_shell.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_server = subparser.add_parser("server", help="Starts the translatepy HTTP server")
    parser_server.add_argument('--port', '-p', action='store', default=5000, type=int, help='port to run the server on')
    parser_server.add_argument('--host', action='store', default="127.0.0.1", type=str, help='host to run the server on')

    args = parser.parse_args()

    if not args.action:
        # required subparser had been added in Python 3.7
        print(NO_ACTION)
        return

    if args.translators is not None:
        dl = translatepy.Translator(args.translators.split(","))
    else:
        dl = translatepy.Translator()

    if args.action == 'translate':
        try:
            result = dl.translate(text=args.text, dest_lang=args.dest_lang, source_lang=args.source_lang)
            print(result.as_json(indent=4, ensure_ascii=False))
        except UnknownLanguage as err:
            print(dumps({
                "success": False,
                "guessedLanguage": err.guessed_language,
                "similarity": err.similarity,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))
        except Exception as err:
            print(dumps({
                "success": False,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))

    elif args.action == 'transliterate':
        try:
            result = dl.transliterate(args.text, args.dest_lang, args.source_lang)
            print(result.as_json(indent=4, ensure_ascii=False))
        except UnknownLanguage as err:
            print(dumps({
                "success": False,
                "guessedLanguage": err.guessed_language,
                "similarity": err.similarity,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))
        except Exception as err:
            print(dumps({
                "success": False,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))

    elif args.action == 'spellcheck':
        try:
            result = dl.spellcheck(args.text, args.source_lang)
            print(result.as_json(indent=4, ensure_ascii=False))
        except UnknownLanguage as err:
            print(dumps({
                "success": False,
                "guessedLanguage": err.guessed_language,
                "similarity": err.similarity,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))
        except Exception as err:
            print(dumps({
                "success": False,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))

    elif args.action == 'language':
        try:
            result = dl.language(args.text)
            print(result.as_json(indent=4, ensure_ascii=False))
        except UnknownLanguage as err:
            print(dumps({
                "success": False,
                "guessedLanguage": err.guessed_language,
                "similarity": err.similarity,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))
        except Exception as err:
            print(dumps({
                "success": False,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))

    # SERVER
    if args.action == "server":
        try:
            from translatepy.server import translation
            from translatepy.server import language
            from translatepy.server.server import app
            from nasse.logging import log, LogLevels
            log("🍡 Press Ctrl+C to quit", LogLevels.INFO)
            app.run(host=args.host, port=args.port)
        except Exception as err:
            from sys import version_info
            if version_info < (3, 4):
                raise VersionNotSupported("Python 3.4 or higher is required to run the server with Nasse") from err
            from os import name
            if name == "nt":
                raise VersionNotSupported("The server can only be ran on Unix-like systems") from err
            raise err

    # INTERACTIVE VERSION
    if args.action == 'shell':
        dest_lang = args.dest_lang
        # source_lang = args.source_lang
        try:
            dest_lang = translatepy.Language(dest_lang)
        except Exception:
            dest_lang = None
        while True:
            answers = inquirer.prompt(actions)
            action = answers["action"]
            if action == "Quit":
                break
            if action in ['Translate', 'Example', 'Dictionary']:
                def _prompt_for_destination_language():
                    answers = inquirer.prompt([
                        inquirer.Text(
                            name='dest_lang',
                            message=INPUT_PREFIX.format(action="Select Lang.")
                        )
                    ])
                    try:
                        dest_lang = translatepy.Language(answers["dest_lang"])
                        print("The selected language is " + dest_lang.name)
                        return dest_lang
                    except Exception:
                        print("\033[93mThe given input doesn't seem to be a valid language\033[0m")
                        return _prompt_for_destination_language()

                if dest_lang is None:
                    if action == "Translate":
                        print("In what language do you want to translate in?")
                    elif action == "Example":
                        print("What language do you want to use for the example checking?")
                    else:
                        print("What language do you want to use for the dictionary checking?")
                    dest_lang = _prompt_for_destination_language()

            print("")
            if action == "Translate":
                print("\033[96mEnter '.quit' to stop translating\033[0m")
                while True:
                    input_text = input(INPUT_PREFIX.format(action="Translate"))
                    if input_text == ".quit":
                        break
                    try:
                        result = dl.translate(input_text, dest_lang, args.source_lang)
                        print("Result \033[90m({source} → {dest})\033[0m: {result}".format(source=result.source_lang, dest=result.dest_lang, result=result.result))
                    except Exception:
                        print_exc()
                        print("We are sorry but an error occured or no result got returned...")

            elif action == "Transliterate":
                print("\033[96mEnter '.quit' to stop transliterating\033[0m")
                while True:
                    input_text = input(INPUT_PREFIX.format(action="Transliterate"))
                    if input_text == ".quit":
                        break
                    try:
                        result = dl.transliterate(text=input_text, dest_lang=dest_lang, source_lang=args.source_lang)
                        print("Result ({lang}): {result}".format(lang=result.source_lang, result=result.result))
                    except Exception:
                        print_exc()
                        print("We are sorry but an error occured or no result got returned...")

            elif action == "Spellcheck":
                print("\033[96mEnter '.quit' to stop spellchecking\033[0m")
                while True:
                    input_text = input(INPUT_PREFIX.format(action="Spellcheck"))
                    if input_text == ".quit":
                        break
                    try:
                        result = dl.spellcheck(input_text, args.source_lang)
                        print("Result ({lang}): {result}".format(lang=result.source_lang, result=result.result))
                    except Exception:
                        print_exc()
                        print("We are sorry but an error occured or no result got returned...")

            elif action == "Language":
                print("\033[96mEnter '.quit' to stop checking for the language\033[0m")
                while True:
                    input_text = input(INPUT_PREFIX.format(action="Language"))
                    if input_text == ".quit":
                        break
                    try:
                        result = dl.language(input_text)
                        try:
                            result = translatepy.Language(result.result).name
                        except Exception:
                            result = result.result
                        print("The given text is in {lang}".format(lang=result))
                    except Exception:
                        print_exc()
                        print("We are sorry but an error occured or no result got returned...")

            elif action == "Example":
                print("\033[96mEnter '.quit' to stop checking for examples\033[0m")
                while True:
                    input_text = input(INPUT_PREFIX.format(action="Example"))
                    if input_text == ".quit":
                        break
                    try:
                        result = dl.example(input_text, dest_lang, args.source_lang)
                        results = []
                        if isinstance(result.result, list):
                            try:
                                results = results[:3]
                            except Exception:
                                results = results
                        else:
                            results = [str(result.result)]
                        if len(results) > 0:
                            print("Here is a list of examples:")
                            for example in results:
                                print("    - " + str(example))
                        else:
                            print("No example found for {input_text}".format(input_text=input_text))
                    except Exception:
                        print("We are sorry but an error occured or no result got returned...")

        print("Thank you for using \033[96mtranslatepy\033[0m!")


if __name__ == "__main__":
    main()
