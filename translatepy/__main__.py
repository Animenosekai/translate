"""
__main__.py

The `translatepy` CLI
"""
import argparse
import json
import webbrowser

import translatepy
from translatepy.exceptions import UnknownLanguage
from translatepy.cli import tui, shell


def entry():
    # Create the parser
    parser = argparse.ArgumentParser(prog='translatepy', description='Translate, transliterate, get the language of texts in no time with the help of numerous APIs!')

    parser.add_argument('--version', '-v', action='version', version=translatepy.__version__)
    parser.add_argument("--translators", action="store", type=str, help="List of translators to use. Each translator name should be comma-separated.", required=False, default=None)

    subparser = parser.add_subparsers(help='Actions', dest="action", required=True)
    parser_tui = subparser.add_parser("tui", help="A nice TUI to use translatepy interactively")

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

    def prepare_server_parser(parser: argparse.ArgumentParser):
        parser.add_argument('--port', '-p', action='store', default=5005, type=int, help='port to run the server on')
        parser.add_argument('--host', action='store', default="127.0.0.1", type=str, help='host to run the server on')
        parser.add_argument('--debug', "-d", action='store_true', help="Runs the server in DEBUG mode")

    parser_server = subparser.add_parser("server", help="Starts the translatepy HTTP server")
    prepare_server_parser(parser_server)

    parser_website = subparser.add_parser("website", help="Starts the translatepy website server")
    prepare_server_parser(parser_website)
    parser_website.add_argument("--headless", action="store_true", help="Avoids opening the website in the default browser")

    args = parser.parse_args()

    if args.translators is not None:
        service = translatepy.Translator(args.translators.split(","))
    else:
        service = translatepy.Translator()

    if args.action == "tui":
        tui.app.TranslatepyTUI().run()

    if args.action == 'translate':
        try:
            result = service.translate(text=args.text, dest_lang=args.dest_lang, source_lang=args.source_lang)
            print(result.as_json(indent=4, ensure_ascii=False))
        except UnknownLanguage as err:
            print(json.dumps({
                "success": False,
                "guessedLanguage": err.guessed_language,
                "similarity": err.similarity,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))
        except Exception as err:
            print(json.dumps({
                "success": False,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))

    elif args.action == 'transliterate':
        try:
            result = service.transliterate(args.text, args.dest_lang, args.source_lang)
            print(result.as_json(indent=4, ensure_ascii=False))
        except UnknownLanguage as err:
            print(json.dumps({
                "success": False,
                "guessedLanguage": err.guessed_language,
                "similarity": err.similarity,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))
        except Exception as err:
            print(json.dumps({
                "success": False,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))

    elif args.action == 'spellcheck':
        try:
            result = service.spellcheck(args.text, args.source_lang)
            print(result.as_json(indent=4, ensure_ascii=False))
        except UnknownLanguage as err:
            print(json.dumps({
                "success": False,
                "guessedLanguage": err.guessed_language,
                "similarity": err.similarity,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))
        except Exception as err:
            print(json.dumps({
                "success": False,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))

    elif args.action == 'language':
        try:
            result = service.language(args.text)
            print(result.as_json(indent=4, ensure_ascii=False))
        except UnknownLanguage as err:
            print(json.dumps({
                "success": False,
                "guessedLanguage": err.guessed_language,
                "similarity": err.similarity,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))
        except Exception as err:
            print(json.dumps({
                "success": False,
                "exception": err.__class__.__name__,
                "error": str(err)
            }, indent=4, ensure_ascii=False))

    # SERVER
    if args.action in ("server", "website"):
        from translatepy.server.endpoints.api import _, language
        
        if args.action == "website":
            from translatepy.server.endpoints.docs import _
            from translatepy.server.endpoints import _
            if not args.headless:
                webbrowser.open(f"http://{args.host}:{args.port}")

        from translatepy.server.server import app
        app.run(host=args.host, port=args.port, debug=args.debug)

    # INTERACTIVE VERSION
    if args.action == 'shell':
        shell.run(args, service)


if __name__ == "__main__":
    entry()
