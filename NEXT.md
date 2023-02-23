---
version: 3.0
status: ALPHA
---

# Next

> Provides informations about the next coming version

This version provides general improvements over the whole project, bringing exciting new features.

## New

- [ ] New built-in translators
  - [ ] [QcriTranslator](https://mt.qcri.org/api)
  - [ ] [Linguee Translator](https://www.linguee.com) [^3]
  - [ ] [PONS Translator](https://en.pons.com/text-translation)
  - [ ] [Papago Translator](https://papago.naver.com)
  - [ ] [Promt Translate](https://www.online-translator.com/translation)
  - [ ] [TranslateDict](https://github.com/Animenosekai/translate/issues/28) [^9]
- [x] A built-in HTTP server [^8]
  - 50a17c5c48612e9aef076f900745e72283c3921d
- [ ] A built-in local website [^2]
  - Refer to branch [`website`](https://github.com/Animenosekai/translate/tree/website) [^10]
- [ ] Bulk translation [^11]
- [ ] Formality and glossary feature from DeepL [^12]
- 🧃 Executables to run *translatepy* without Python

<!-- Reverso
Translate.com -->

## Fixes

- [x] Fixing Reverso
  - 834cf6eaa1c0775e1d6de23294ce0465082b0bf1
- [x] Fixing Yandex.Translate
  - b7690dc3eda80aa6ea5731d54d89255e44ea6f2f
- [x] Fixing Bing Translate
  - c71b6c3fee596160dd291ceda283b91b729c1bec
  - dfc2f05 (#72)
- [ ] Added a new endpoint to Microsoft Translate [^7]
<!-- - Fixing Google Translate -->

## Updates

- [ ] New `dictionary`, `example` methods [^5]
- [ ] New `alternative` method [^5]
- [ ] Redesigning the models (ex: `raw` attribute)
- [ ] Using a new size-limited LRU system (#76) [^6]
- [ ] A brand new CLI [^1]
- [ ] Improved type hinting
- [ ] Improved in-code documentation, following the [Miko Docs](https://github.com/Animenosekai/miko) style from now on
- [x] Dynamic translator import [^4]

Everything is detailed in the [`README.md`](./README.md) file

A comparison from the previous release can be found here [`v2.3...v3.0`](https://github.com/Animenosekai/nasse/compare/v2.3...v3.0)

A comparison from the current branch can be found here [`v3.0...main`](https://github.com/Animenosekai/nasse/compare/v3.0...main)

[^1]: We might use [*Textual*](https://github.com/Textualize/textual) for an interactive TUI. We should also default to the interactive TUI when running `translatepy` without any action specified.

[^2]: An actual public website was planned but due to the end of Heroku's free service and a lack of resource for now, we are going to stick with the local website (I think?). However the idea is not abandonned and a way of ranking the different translators based on real results is expected in the future.

[^3]: For single word translations

[^4]: This provides a way of choosing the translators to use from the CLI (#53)
  But this also allows choosing the translator from the web server and thus the website.

[^5]: Refer to <https://github.com/Animenosekai/translate/discussions/62>

[^6]: Following #58

[^7]: Following <https://github.com/Animenosekai/translate/issues/28#issuecomment-918746811>

[^8]: Following #54

[^9]: Following #28

[^10]: The branch needs to be changed to fit the [`main`](https://github.com/Animenosekai/translate) branch (local website) and to have a CLI access

[^11]: Following #66

[^12]: Following #65

> **Note**  
> Ideas with a `🧃` mark in front still need some consideration and might not be in the final product.

> 🍡 Animenosekai
