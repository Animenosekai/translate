---
version: 3.0
status: ALPHA
---

# Next

> Provides informations about the next coming version

This version provides general improvements over the whole project, bringing exciting new features.

## New

- New built-in translators
  - [QcriTranslator](https://mt.qcri.org/api)
  - [Linguee Translator](https://www.linguee.com) (for single word translations)
  - [PONS Translator](https://en.pons.com/text-translation)
  - [Papago Translator](https://papago.naver.com)
  - [Promt Translate](https://www.online-translator.com/translation)
  - [TranslateDict](https://github.com/Animenosekai/translate/issues/28)
- A built-in HTTP server
- A built-in local website [^2]
- Bulk translation
- Formality and glossary feature from DeepL
- 🧃 Executables to run *translatepy* without Python

<!-- Reverso
Translate.com -->

## Fixes

- Fixing Reverso
- Fixing Yandex.Translate
- Fixing Bing Translate
<!-- - Fixing Google Translate -->

## Updates

- New `dictionary`, `example` methods
- New `alternative` method
- Redesigning the models (ex: `raw` attribute)
- Using a new size-limited LRU system
- A brand new CLI [^1]
- Improved type hinting
- Improved in-code documentation, following the [Miko Docs](https://github.com/Animenosekai/miko) style from now on
- Dynamic translator import

Everything is detailed in the [`README.md`](./README.md) file

A comparison from the previous release can be found here [`v2.3...v3.0`](https://github.com/Animenosekai/nasse/compare/v2.3...v3.0)

A comparison from the current branch can be found here [`v3.0...main`](https://github.com/Animenosekai/nasse/compare/v3.0...main)

[^1]: We might use [*Textual*](https://github.com/Textualize/textual) for an interactive TUI. We should also default to the interactive TUI when running `translatepy` without any action specified.

[^2]: An actual public website was planned but due to the end of Heroku's free service and a lack of resource for now, we are going to stick with the local website (I think?). However the idea is not abandonned and a way of ranking the different translators based on real results is expected in the future.

> **Note**  
> Ideas with a `🧃` mark in front still need some consideration and might not be in the final product.

> 🍡 Animenosekai
