import cmd
import typing

from nasse import logger

import translatepy
from translatepy.cli.shell.colors import TC


class TranslatepyShell(cmd.Cmd):
    """the shell implementation for translatepy"""

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
