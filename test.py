from translatepy.translators.papago import Papago
from rich.console import Console

console = Console()

try:
    p = Papago()
    # t = p.translate("Hello world", "Japanese")
    # print(t.__pretty__(cli=True))
    r = p.text_to_speech("こんにちは", source_lang="Japanese")
    r.write_to_file(f"hello.{r.extension}")
except Exception:
    console.print_exception(show_locals=True)
