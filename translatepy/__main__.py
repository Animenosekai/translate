import argparse
import translatepy


def main():
    dl = translatepy.Translator()

    # Create the parser
    parser = argparse.ArgumentParser(prog='translatepy-cli', description='Translate, transliterate, get the language of texts in no time with the help of multiple APIs!')

    parser.add_argument('--version', action='version', version=translatepy.__version__)

    subparser = parser.add_subparsers(help='Actions', dest="action", required=True)

    parser_translate = subparser.add_parser('translate', help='Translates the given text to the given language')
    parser_translate.add_argument('--text', '-t', action='store', type=str, required=True, help='text to translate')
    parser_translate.add_argument('--dest-lang', '-d', action='store', type=str, required=True, help='destination language')
    parser_translate.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    parser_shell = subparser.add_parser('shell', help='Translates the given text in interactive shell mode')
    parser_shell.add_argument('--dest-lang', '-d', action='store', type=str, required=True, help='destination language')
    parser_shell.add_argument('--source-lang', '-s', action='store', default='auto', type=str, help='source language')

    args = parser.parse_args()

    if args.action == 'translate':
        result = dl.translate(args.text, args.dest_lang, args.source_lang)
        print(result)

    if args.action == 'shell':
        while True:
            input_text = input(">>> ")

            result = dl.translate(input_text, args.dest_lang, args.source_lang)
            print(result)


if __name__ == "__main__":
    main()
