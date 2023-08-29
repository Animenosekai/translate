from translatepy.translators.microsoft import MicrosoftTranslateV3
from rich.console import Console

from loguru import logger

console = Console()

try:
    p = MicrosoftTranslateV3()
    # t = p.translate("Hello world", "Japanese")
    # print(t.__pretty__(cli=True))
    # r = p.text_to_speech("こんにちは", source_lang="Japanese")
    r = p.text_to_speech("Удобно автоматизировать работу ", source_lang="ru")
    r.write_to_file(f"hello.{r.extension}")
except Exception as ex:
    logger.exception(ex)
    # console.print_exception(show_locals=True)
