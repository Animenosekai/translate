import argparse
import translatepy
import inquirer
from json import dumps
from traceback import print_exc

INPUT_PREFIX = "(\033[90mtranslatepy ~ \033[0m{action}) > "

actions = [
    inquirer.List(
        name='action',
        message="What do you want to do?",
        choices=['Translate', 'Transliterate', 'Spellcheck', 'Language', 'Example', 'Quit'],
        carousel=True
    )
]

def main():
    dl = translatepy.Translator()

    # Create the parser
    parser = argparse.ArgumentParser(prog='translatepy', description='Translate, transliterate, get the language of texts in no time with the help of multiple APIs!')

    parser.add_argument('--version', '-v', action='version', version=translatepy.__version__)

    subparser = parser.add_subparsers(help='Actions', dest="action", required=True)

    parser_translate = subparser.add_parser('translate', help='Translates the given text to the given language')
    parser_translate.add_argument('--text', '-t', action='store', type=str, required=True, help='text to translate')
    parser_translate.add_argument('--dest-lang', '-d', action='store', type=str, required=True, help='destination language')
    parser_translate.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_transliterate = subparser.add_parser('transliterate', help='Transliterates the given text')
    parser_transliterate.add_argument('--text', '-t', action='store', type=str, required=True, help='text to transliterate')
    parser_transliterate.add_argument('--dest-lang', '-d', action='store', type=str, default="en", help='destination language')
    parser_transliterate.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_spellcheck = subparser.add_parser('transliterate', help='Checks the spelling of the given text')
    parser_spellcheck.add_argument('--text', '-t', action='store', type=str, required=True, help='text to spellcheck')
    parser_spellcheck.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_language = subparser.add_parser('language', help='Checks the language of the given text')
    parser_language.add_argument('--text', '-t', action='store', type=str, required=True, help='text to check the language')

    parser_shell = subparser.add_parser('shell', help="Opens translatepy's interactive mode")
    parser_shell.add_argument('--dest-lang', '-d', action='store', default=None, type=str, help='destination language')
    parser_shell.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    args = parser.parse_args()

    if args.action == 'translate':
        result = dl.translate(args.text, args.dest_lang, args.source_lang)
        print(dumps(result.__dict__, indent=4, ensure_ascii=False))

    elif args.action == 'transliterate':
        result = dl.transliterate(args.text, args.dest_lang, args.source_lang)
        print(dumps(result.__dict__, indent=4, ensure_ascii=False))

    elif args.action == 'spellcheck':
        result = dl.spellcheck(args.text, args.source_lang)
        print(dumps(result.__dict__, indent=4, ensure_ascii=False))

    elif args.action == 'language':
        result = dl.language(args.text)
        print(dumps(result.__dict__, indent=4, ensure_ascii=False))


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
                    answers = inquirer.prompt([
                        inquirer.Text(
                            name='destination_language',
                            message=INPUT_PREFIX.format(action="Select Lang.")
                        )
                    ])
                    try:
                        destination_language = translatepy.Language(answers["destination_language"])
                        print("The selected language is " + destination_language.english)
                        return destination_language
                    except Exception:
                        print("\033[93mThe given input doesn't seem to be a valid language\033[0m")
                        return _prompt_for_destination_language()

                if destination_language is None:
                    if action == "Translate":
                        print("In what language do you want to translate in?")
                    elif action == "Example":
                        print("What language do you want to use for the example checking?")
                    else:
                        print("What language do you want to use for the dictionary checking?")
                    destination_language = _prompt_for_destination_language()

            print("")
            if action == "Translate":
                print("\033[96mEnter '.quit' to stop translating\033[0m")
                while True:
                    input_text = input(INPUT_PREFIX.format(action="Translate"))
                    if input_text == ".quit":
                        break
                    try:
                        result = dl.translate(input_text, destination_language, args.source_lang)
                        print("Result \033[90m({source} → {dest})\033[0m: {result}".format(source=result.source_language, dest=result.destination_language, result=result.result))
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
                        result = dl.transliterate(text=input_text, destination_language=destination_language, source_language=args.source_lang)
                        print("Result ({lang}): {result}".format(lang=result.source_language, result=result.result))
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
                        print("Result ({lang}): {result}".format(lang=result.source_language, result=result.result))
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
                            result = translatepy.Language(result.result).english
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
                        result = dl.example(input_text, destination_language, args.source_lang)
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
