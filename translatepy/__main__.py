"""
__main__.py

The `translatepy` CLI
"""
import argparse
import webbrowser
from argparse import Action

from nasse.exceptions import NasseException
from nasse.utils.formatter import format as nasse_format
from nasse.utils.json import encoder, minified_encoder

import translatepy
from translatepy.cli import sdk, shell, tui
from translatepy.exceptions import UnknownLanguage

ACTIONS_DESCRIPTION = nasse_format("""
  {{tui,translate,translate-html,transliterate,spellcheck,language,example,dictionary,tts,shell,server,website,sdk}}

    ╭─────────────╮
    │   Actions   │
    ╰─────────────╯

    User Interface
    {grey}--------------{normal}
    {blue}tui{normal}                 A nice TUI to use translatepy interactively
    {blue}shell{normal}               Opens translatepy's interactive mode
    {blue}website{normal}             Starts the translatepy website server

    JSON formatted
    {grey}--------------{normal}
    {magenta}translate{normal}           Translates the given text to the given language
    {magenta}translate-html{normal}      Translates the given HTML to the given language
    {magenta}transliterate{normal}       Transliterates the given text
    {magenta}spellcheck{normal}          Checks the spelling of the given text
    {magenta}language{normal}            Checks the language of the given text
    {magenta}example{normal}             Get an examples for the given text
    {magenta}dictionary{normal}          Get meanings for the given text
    {magenta}tts{normal}                 Get text to speech synthesis of the given text

    Developer
    {grey}---------{normal}
    {cyan}server{normal}              Starts the translatepy HTTP server 🌐
    {cyan}sdk{normal}                 Software Development Kit for `translatepy` 🕊️
""")


class TranslatepyHelpFormatter(argparse.HelpFormatter):
    """Formats the help message for `translatepy`"""

    def _format_action(self, action: Action) -> str:
        if isinstance(action, argparse._SubParsersAction):
            return ACTIONS_DESCRIPTION
        return super()._format_action(action)


def entry():
    """the CLI entrypoint"""
    # Create the parser
    # parser = argparse.ArgumentParser(prog='translatepy', description='Translate, transliterate, get the language of texts in no time with the help of numerous APIs!')
    parser = argparse.ArgumentParser(prog='translatepy',
                                     description='🍡 \033[1mTranslate, transliterate, get the language of texts in no time with the help of numerous APIs!\033[0m',
                                     formatter_class=TranslatepyHelpFormatter)

    parser.add_argument('--version', '-v', action='version', version=translatepy.__version__)
    parser.add_argument("--translators", action="store", type=str, help="List of translators to use. Each translator name should be comma-separated.", required=False, default=None)

    subparser = parser.add_subparsers(help='Actions', dest="action", required=False)
    parser_tui = subparser.add_parser("tui", help="A nice TUI to use translatepy interactively")

    def prepare_json_parser(parser: argparse.ArgumentParser):
        parser.add_argument("text", action="store", type=str, help="The text to work with")
        parser.add_argument("--minified", "--mini", action="store_true", help="To minify the resulting JSON")

    parser_translate = subparser.add_parser('translate', help='Translates the given text to the given language')
    prepare_json_parser(parser_translate)
    parser_translate.add_argument('--dest-lang', '-d', action='store', type=str, required=True, help='destination language')
    parser_translate.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_translate_html = subparser.add_parser('translate-html', help='Translates the given HTML to the given language')
    prepare_json_parser(parser_translate_html)
    parser_translate_html.add_argument('--dest-lang', '-d', action='store', type=str, required=True, help='destination language')
    parser_translate_html.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')
    parser_translate_html.add_argument('--parser', action='store', default='html.parser', type=str, help='the HTML parser to use')
    parser_translate_html.add_argument('--threads-limit', action='store', default=100, type=int, help='the maximum number of threads to spawn to translate the HTML nodes')
    parser_translate_html.add_argument('--strict', action='store_true', help="if it should error out if any of the nodes couldn't be translated")

    parser_transliterate = subparser.add_parser('transliterate', help='Transliterates the given text')
    prepare_json_parser(parser_transliterate)
    parser_transliterate.add_argument('--dest-lang', '-d', action='store', type=str, default="en", help='destination language')
    parser_transliterate.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_spellcheck = subparser.add_parser('spellcheck', help='Checks the spelling of the given text')
    prepare_json_parser(parser_spellcheck)
    parser_spellcheck.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_language = subparser.add_parser('language', help='Checks the language of the given text')
    prepare_json_parser(parser_language)

    parser_example = subparser.add_parser('example', help='Get an examples for the given text')
    prepare_json_parser(parser_example)
    parser_example.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_dictionary = subparser.add_parser('dictionary', help='Get meanings for the given text')
    prepare_json_parser(parser_dictionary)
    parser_dictionary.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_tts = subparser.add_parser('tts', help='Get text to speech synthesis of the given text')
    prepare_json_parser(parser_tts)
    parser_tts.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

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

    parser_sdk = subparser.add_parser("sdk", help="Software Development Kit for `translatepy` 🕊️")
    sdk.prepare_argparse(parser_sdk)

    args = parser.parse_args()

    if args.action == "sdk":
        sdk.entry(args=args)

    if args.translators:
        service = translatepy.Translator(args.translators.split(","))
    else:
        service = translatepy.Translator()

    args.action = args.action or "tui"

    if args.action == "tui":
        tui.app.TranslatepyTUI().run()

    def apply(work: str, **kwargs):
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
            result = getattr(service, work)(**kwargs)
            # might add `success: true`
            print(json_encoder.encode(result.exported))
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

    if args.action == 'translate':
        return apply("translate", text=args.text, dest_lang=args.dest_lang, source_lang=args.source_lang)
    if args.action == 'translate-html':
        return apply("translate-html", text=args.text, dest_lang=args.dest_lang, source_lang=args.source_lang,
                     parser=args.parser, threads_limit=args.threads_limit, strict=args.strict)
    elif args.action == 'transliterate':
        return apply("transliterate", text=args.text, dest_lang=args.dest_lang, source_lang=args.source_lang)
    elif args.action == 'spellcheck':
        return apply("spellcheck", text=args.text, source_lang=args.source_lang)
    elif args.action == 'language':
        return apply("language", text=args.text)
    elif args.action == 'example':
        return apply("example", text=args.text, source_lang=args.source_lang)
    elif args.action == 'dictionary':
        return apply("dictionary", text=args.text, source_lang=args.source_lang)
    elif args.action == 'tts':
        return apply("text_to_speech", text=args.text, source_lang=args.source_lang)

    # SERVER
    if args.action in ("server", "website"):
        from translatepy.server.endpoints.api import _, language

        if args.action == "website":
            from translatepy.server.endpoints import _
            from translatepy.server.endpoints.docs import _
            if not args.headless:
                webbrowser.open(f"http://{args.host}:{args.port}")

        from translatepy.server.server import app
        app.run(host=args.host, port=args.port, debug=args.debug)

    # INTERACTIVE VERSION
    if args.action == 'shell':
        shell.run(args, service)


if __name__ == "__main__":
    entry()
