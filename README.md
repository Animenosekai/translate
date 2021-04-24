# `translatepy` (originally: translate)

### An aggregation of multiple translation API.  
***Translate, transliterate, get the language of texts in no time with the help of multiple APIs!***

[![PyPI version](https://badge.fury.io/py/translatepy.svg)](https://pypi.org/project/translatepy/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/translatepy)](https://pypistats.org/packages/translatepy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/translatepy)](https://pypi.org/project/translatepy/)
[![PyPI - Status](https://img.shields.io/pypi/status/translatepy)](https://pypi.org/project/translatepy/)
[![GitHub - License](https://img.shields.io/github/license/Animenosekai/translate)](https://github.com/Animenosekai/translate/blob/master/LICENSE)
[![GitHub top language](https://img.shields.io/github/languages/top/Animenosekai/translate)](https://github.com/Animenosekai/translate)
[![CodeQL Checks Badge](https://github.com/Animenosekai/translate/workflows/CodeQL%20Python%20Analysis/badge.svg)](https://github.com/Animenosekai/translate/actions?query=workflow%3ACodeQL)
[![Pytest](https://github.com/Animenosekai/translate/actions/workflows/pytest.yml/badge.svg)](https://github.com/Animenosekai/translate/actions/workflows/pytest.yml)
![Code Size](https://img.shields.io/github/languages/code-size/Animenosekai/translate)
![Repo Size](https://img.shields.io/github/repo-size/Animenosekai/translate)
![Issues](https://img.shields.io/github/issues/Animenosekai/translate)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need Python 3 to use this module

```bash
# vermin output
Minimum required versions: 3.2
Incompatible versions:     2
```

According to Vermin (`--backport typing`), Python 3.2 is needed for the backport of typing but some may say that it is available for python versions higher than 3.0

Always check if your Python version works with `translatepy` before using it in production

### Installing

You can install it from PyPI with:

```bash
pip install translatepy
```

You can check if you successfully installed it by printing out its version:

```bash
python -c "import translatepy; print(translatepy.__version__)"
# output:
translatepy v1.5.2
```

## List of Services

- [Microsoft Bing Translator](https://www.bing.com/translator)
- [Google Translate](https://translate.google.com)
- [Yandex Translate](https://translate.yandex.com)
- [Reverso](https://www.reverso.net/text_translation.aspx)
- [DeepL](https://www.deepl.com/translator)

All of the names belong to their respective rightholders.


## Usage
```python
>>> import translatepy
>>> translator = translatepy.Translator()
>>> translator.translate("Hello", "French")
'Bonjour' (type: TranslationResult)
>>> translator.language("こんにちは")
'Japanese' (type: Language)
```

### The Language Class
The language class contains lots of information about a language.

You need to pass the language name or code to the class initialization:
```python
translatepy.Language("French")
# Returns a Language class with the "fr" language
translatepy.Language("en")
# Returns a Language class with the "en" language
translatepy.Language("eng")
# Returns a Language class with the "en" language
translatepy.Language("日本語")
# Returns a Language class with the "ja" language
```

The Language Class contains both the ISO 639-1 Alpha-2 language code and the ISO 639-2 Alpha-3 language code (the latter is nullable)

It also contains the language name for all of the languages available. (nullable)

Example:
```python
>>> translatepy.Language("日本語").french
'Japonais'
```

It contains the correct language code for each translation service

It also contains the "similarity" attribute which gives back a number between 0 and 1 and which shows the similarity of the input language with what it found in the language code database.

A `translatepy.models.exceptions.UnknownLanguage` exception is raised if the given language is unknown.

——> A language with low chance of being the one you've chosen is displayed along with its similarity

### The TranslationResult Class
This class contains all of the information needed to get the result of a translation:

- source: The input text
- result: The translation result
- source_language: The input language
- destination_language: The result language
- service: The source (service used)

### Caching
All of the operations are cached to provide the best performances

You can empty the cache by giving the default value to the variables holding the caches:

```python
translatepy.TRANSLATION_CACHES = {}
translatepy.TRANSLITERATION_CACHES = {}
translatepy.SPELLCHECK_CACHES = {}
translatepy.LANGUAGE_CACHES = {}
translatepy.EXAMPLE_CACHES = {}
translatepy.DICTIONNARY_CACHES = {}
```

Or by calling the `Translator()` method "`clean_cache`"

***Warning: `translatepy`'s caches are global: they are used through all instances of `Translator()`***

### The Translator Class
It is the High API providing all of the methods and optimizations for `translatepy`
- translate: To translate things
- transliterate: To transliterate things
- spellcheck: To check the spelling of a text
- language: To get the language of a text
- example: To get examples of a word
- dictionary: To get a list of translations categorized into "featured" and "less common" by DeepL and Linguee

When something goes wrong or nothing got found, `None` is returned.

The source language while being most of the time an instance of the Language class can sometimes be a string if the conversion to the Language class failed.


An additional `"text_to_speech"` function can be found in the GoogleTranslate class (accessible with the `Translator()` class at `Translator().google_translate`).  
***It is not officialy supported and is not very stable.***


## Deployment

This module is currently in development and might contain bugs.

Feel free to use it in production if you feel like it is suitable for your production even if you may encounter issues.

## Built With

* [safeIO](https://github.com/Animenosekai/safeIO) - To read files
* [pyuseragents](https://github.com/Animenosekai/useragents) - To generate the "User-Agent" HTTP header
* [requests](https://github.com/psf/requests) - To make HTTP requests
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - To parse HTML

## Authors

* **Anime no Sekai** - *Initial work* - [Animenosekai](https://github.com/Animenosekai)

## License

This project is licensed under the GNU Affero General Public License v3.0 License - see the [LICENSE](LICENSE) file for details

### Dataset
All of the datasets are the result of my searches, computation and sometimes translation.

Please ask me if you want to use them in another project.

(`_languages_name_to_code_international.json` comes from Google Translate translations (fixed by me sometimes) and other sourcecs and took me about 8 to 10 hours of work to get it done)

## Acknowledgments

* Thanks to @NawtJ0sh for giving me the way to add Microsoft Bing Translate
* Inspired by py-googletrans (by @ssut) (especially the thread: [Issue #268](https://github.com/ssut/py-googletrans/issues/268))
