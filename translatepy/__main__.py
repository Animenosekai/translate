"""
__main__.py

The `translatepy` CLI
"""
import argparse
import cmd
import json
import typing

import inquirer
from nasse import logger

import translatepy
from translatepy.exceptions import UnknownLanguage


class TC:
    GREY = "\033[90m"
    CYAN = "\033[96m"
    ORANGE = "\033[33m"
    NC = "\033[0m"


INPUT_PREFIX = f"({TC.GREY}translatepy ~ {TC.NC}{{action}}) > "

actions = [
    inquirer.List(
        name='action',
        message="What do you want to do?",
        choices=['Translate', 'Transliterate', 'Spellcheck', 'Language', 'Example', 'Quit'],
        carousel=True
    )
]


def entry():
    # Create the parser
    parser = argparse.ArgumentParser(prog='translatepy', description='Translate, transliterate, get the language of texts in no time with the help of numerous APIs!')

    parser.add_argument('--version', '-v', action='version', version=translatepy.__version__)
    parser.add_argument("--translators", action="store", type=str, help="List of translators to use. Each translator name should be comma-separated.", required=False, default=None)

    subparser = parser.add_subparsers(help='Actions', dest="action", required=True)

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

    if args.translators is not None:
        service = translatepy.Translator(args.translators.split(","))
    else:
        service = translatepy.Translator()

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
    if args.action == "server":
        from translatepy.server.endpoints import _, language
        from translatepy.server.server import app
        app.run(host=args.host, port=args.port)

    # INTERACTIVE VERSION
    if args.action == 'shell':
        destination_language = args.dest_lang
        # source_language = args.source_lang

        try:
            destination_language = translatepy.Language(destination_language)
        except Exception:
            destination_language = None

        while True:
            answers = inquirer.prompt(actions)
            action = answers["action"]
            if action == "Quit":
                break
            if action in ['Translate', 'Example', 'Dictionary']:
                def _prompt_for_destination_language():
                    try:
                        answers = inquirer.prompt([
                            inquirer.Text(
                                name='destination_language',
                                message=INPUT_PREFIX.format(action="Select Lang.")
                            )
                        ], raise_keyboard_interrupt=True)
                    except KeyboardInterrupt:
                        print(f"{TC.CYAN}Operation was interrupted, exit...{TC.NC}")
                        exit(1)

                    try:
                        destination_language = translatepy.Language(answers["destination_language"])
                        print("The selected language is " + destination_language.name)
                        return destination_language
                    except Exception:
                        print(f"{TC.CYAN}The given input doesn't seem to be a valid language{TC.NC}")
                        return _prompt_for_destination_language()

                if destination_language is None:
                    if action == "Translate":
                        print("In what language do you want to translate in?")
                    elif action == "Example":
                        print("What language do you want to use for the example checking?")
                    else:
                        print("What language do you want to use for the dictionary checking?")
                    destination_language = _prompt_for_destination_language()

            intro_msg = f"{TC.CYAN}Enter '.quit' to exit shell mode{TC.NC}"
            cmd_shell = TranslatepyShell(intro_msg=intro_msg, dest_lang=destination_language, prompt=INPUT_PREFIX.format(action=action), service=service, default_cmd=action.lower())

            cmd_shell.cmdloop()


class TranslatepyShell(cmd.Cmd):
    def __init__(self,
                 intro_msg: str,
                 prompt: str,
                 dest_lang: translatepy.Language,
                 service: typing.Optional[translatepy.Translate] = None,
                 default_cmd: typing.Optional[str] = None,
                 cmd_prefix: str = "."):
        super().__init__()

        self.intro = intro_msg
        self.prompt = prompt
        self.cmd_prefix = cmd_prefix
        self.service = service or translatepy.Translate()

        if default_cmd:
            if not (default_cmd_func := self._get_cmd_func(default_cmd)):
                raise ValueError(f"No such command: {default_cmd}")
        else:
            default_cmd_func = None
        self.default_cmd_func = default_cmd_func

        self.destination_language = dest_lang
        self.source_language = 'auto'

    def _get_cmd_func(self, cmd: str) -> typing.Callable:
        return getattr(self, f'do_{cmd}', None)

    def _safe_exec(self, function: typing.Callable, *args, **kwargs) -> typing.Any:
        try:
            return function(*args, **kwargs)
        except Exception:
            logger.print_exception()
            print("We are sorry but an error occured or no result got returned...")

    def default(self, line: str) -> None:
        if line.startswith(self.cmd_prefix):
            cmd = line.split(self.cmd_prefix)[1]
            # cmd = line_cmd.split(" ")[0]
            # cmd_arg = line_cmd.split(" ")[1:]
            func = self._get_cmd_func(cmd)
            if func:
                return self._safe_exec(func, line)
            else:
                print(f"{TC.ORANGE}No such command: {cmd}{TC.NC}")
        elif self.default_cmd_func:
            return self._safe_exec(self.default_cmd_func, line)
        else:
            print(f"{TC.ORANGE}Unknown command line{TC.NC}")

    def do_quit(self, line: str) -> bool:
        print(f"Thank you for using {TC.CYAN}translatepy{TC.NC}!")
        return True

    def do_set_cmd(self, cmd: str):
        func = self._get_cmd_func(cmd.lower())
        if func:
            self.default_cmd_func = func
            self.prompt = cmd
        else:
            print(f"{TC.ORANGE}No such command: {cmd}{TC.NC}")

    def do_transliterate(self, input_text: str):
        result = self.service.transliterate(input_text, self.destination_language, self.source_language)
        print(result.__pretty__(cli=True))

    def do_translate(self, input_text: str):
        result = self.service.translate(input_text, self.destination_language, self.source_language)
        print(result.__pretty__(cli=True))

    def do_spellcheck(self, input_text: str):
        result = self.service.spellcheck(input_text, self.source_language)
        print(result.__pretty__(cli=True))

    def do_language(self, input_text: str):
        result = self.service.language(input_text)
        print(result.__pretty__(cli=True))

    def do_example(self, input_text: str):
        results = self.service.example(input_text, self.destination_language, self.source_language)
        if len(results) > 0:
            print("Here is a list of examples:")
            for example in results:
                print("    - " + str(example.__pretty__(cli=True)))
        else:
            print(f'No example found for "{input_text}"')


if __name__ == "__main__":
    entry()
