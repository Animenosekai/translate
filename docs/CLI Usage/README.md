# CLI Usage

You can also use translatepy from the CLI, using an interactive shell or JSON formatted responses.

## Index

- [Shell](./Shell.md)
- [JSON](./JSON.md)
- [Server](./Server.md)

## Help

```swift
🧃❯ translatepy -h                                                           
usage: translatepy [-h] [--version] [--translators TRANSLATORS] {translate,transliterate,spellcheck,language,shell,server} ...

Translate, transliterate, get the language of texts in no time with the help of multiple APIs!

positional arguments:
  {translate,transliterate,spellcheck,language,shell,server}
                        Actions
    translate           Translates the given text to the given language
    transliterate       Transliterates the given text
    spellcheck          Checks the spelling of the given text
    language            Checks the language of the given text
    shell               Opens translatepy's interactive mode
    server              Starts the translatepy HTTP server

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show program's version number and exit
  --translators TRANSLATORS
                        List of translators to use. Each translator name should be comma-separated.
```