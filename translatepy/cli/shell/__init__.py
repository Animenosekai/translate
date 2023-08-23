import argparse
import translatepy
import inquirer
from translatepy.cli.shell.colors import TC
from translatepy.cli.shell.shell import TranslatepyShell

actions = [
    inquirer.List(
        name='action',
        message="What do you want to do?",
        choices=['Translate', 'Transliterate', 'Spellcheck', 'Language', 'Example', 'Quit'],
        carousel=True
    )
]


INPUT_PREFIX = f"({TC.GREY}translatepy ~ {TC.NC}{{action}}) > "


def run(args: argparse.Namespace, service: translatepy.Translate):
    """Prepares and runs the shell"""
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
