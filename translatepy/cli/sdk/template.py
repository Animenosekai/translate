"""Keeps code templates"""

TRANSLATOR_TEMPLATE = '''\
"""
translatepy's implementation of {name}
"""
import typing

from translatepy import exceptions, models
from translatepy.language import Language
from translatepy.translators.base import (BaseTranslateException,
                                          BaseTranslator, C)
from translatepy.utils import request

class {class_name}Exception(BaseTranslateException):
    error_codes = {{
        429: "Too many requests" # add your own status codes and error
    }}

    # you can use it like so in your endpoint:
    # raise {class_name}Exception(request.status_code)

class {class_name}(BaseTranslator):
    """
    translatepy's implementation of {name}
    """

    # These codes are the translator's codes, as returned for example by `_language_to_code`
    _supported_languages = {{"set", "of", "supported", "language", "code", "eng", "fra", "jpa"}}

    def __init__(self, session: typing.Optional[request.Session] = None, *args, **kwargs):
        super().__init__(session, *args, **kwargs)

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, *args, **kwargs) -> models.TranslationResult[C]:
        # replace this to return a `TranslationResult`
        return super()._translate(text, dest_lang, source_lang, *args, **kwargs)

    def _alternatives(self: C, translation: models.TranslationResult, *args, **kwargs) -> typing.Union[models.TranslationResult[C], typing.List[models.TranslationResult[C]]]:
        return super()._alternatives(translation, *args, **kwargs)

    def _transliterate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, *args, **kwargs) -> models.TransliterationResult[C]:
        return super()._transliterate(text, dest_lang, source_lang, *args, **kwargs)

    def _spellcheck(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[models.SpellcheckResult[C], models.RichSpellcheckResult[C]]:
        return super()._spellcheck(text, source_lang, *args, **kwargs)

    def _language(self: C, text: str, *args, **kwargs) -> models.LanguageResult[C]:
        return super()._language(text, *args, **kwargs)

    def _example(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[models.ExampleResult[C], typing.List[models.ExampleResult[C]]]:
        return super()._example(text, source_lang, *args, **kwargs)

    def _dictionary(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]], typing.List[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]]]]:
        return super()._dictionary(text, source_lang, *args, **kwargs)

    def _text_to_speech(self: C, text: str, speed: int, gender: models.Gender, source_lang: typing.Any, *args, **kwargs) -> models.TextToSpeechResult[C]:
        return super()._text_to_speech(text, speed, gender, source_lang)

    def _code_to_language(self, code: typing.Union[str, typing.Any], *args, **kwargs) -> Language:
        return super()._code_to_language(code, *args, **kwargs) # language code to translatepy.Language

    def _language_to_code(self, language: Language, *args, **kwargs) -> typing.Union[str, typing.Any]:
        return super()._language_to_code(language, *args, **kwargs) # translatepy.Language to language code
'''
"""A template to create new translators (format: 'name', 'class_name')"""

INIT_TEMPLATE = '''\
'''
"""A template for __init__.py files"""

README_TEMPLATE = '''\
# {name}

A translatepy implementation of {name}

[![PyPI version](https://badge.fury.io/py/{name}.svg)](https://pypi.org/project/{name}/)
[![Downloads](https://static.pepy.tech/personalized-badge/{name}?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/{name})
[![PyPI - Downloads](https://img.shields.io/pypi/dm/{name})](https://pypistats.org/packages/{name})
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{name})](https://pypi.org/project/{name}/)
[![PyPI - Status](https://img.shields.io/pypi/status/{name})](https://pypi.org/project/{name}/)
[![GitHub - License](https://img.shields.io/github/license/{author}/{name})](https://github.com/{author}/{name}/blob/master/LICENSE)
[![GitHub top language](https://img.shields.io/github/languages/top/{author}/{name})](https://github.com/{author}/{name})
[![CodeQL Checks Badge](https://github.com/{author}/{name}/workflows/CodeQL%20Python%20Analysis/badge.svg)](https://github.com/{author}/{name}/actions?query=workflow%3ACodeQL)
[![Pytest](https://github.com/{author}/{name}/actions/workflows/pytest.yml/badge.svg)](https://github.com/{author}/{name}/actions/workflows/pytest.yml)
![Code Size](https://img.shields.io/github/languages/code-size/{author}/{name})
![Repo Size](https://img.shields.io/github/repo-size/{author}/{name})
![Issues](https://img.shields.io/github/issues/{author}/{name})

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need Python 3 to use this module

```bash
# vermin output
Minimum required versions: 3.8
Incompatible versions:     2
```

Always check if your Python version works with `{name}` before using it in production

## Installing

### Option 1: From PyPI

```bash
pip install --upgrade {name}
```

### Option 2: From Git

```bash
pip install --upgrade git+https://github.com/{author}/{name}
```

You can check if you successfully installed it by printing out its version:

```bash
$ python -c "import {name}; print({name}.__version__)"
# output:
1.0
```

## Usage

### Directly

You can use it directly as a translator:

```python
>>> from {name} import {class_name}
>>> t = {class_name}()
>>> t.translate("Hello world", "Japanese")
```

### In a translator aggregator

But you can also use it in a translator aggregator:

```python
>>> from {name} import {class_name}
>>> from translatepy import Translator
>>> from translatepy.translators import GoogleTranslate, DeeplTranslate, YandexTranslate
>>> t = Translator([{class_name}, GoogleTranslate, DeeplTranslate, YandexTranslate])
>>> t.translate("Hello world", "Japanese")
```

## Caching

All of the operations are cached to provide the best performances

You can empty the cache by calling the `clean_cache` method.

## Deployment

This module is currently in development and might contain bugs.

## Contributing

Pull requests are welcome. For major changes, please open an discussion first to discuss what you would like to change.

Please make sure to update the tests accordingly.

## Built With

- [translatepy]({translatepy_repo})

## Authors

- **{author}** - *Initial work* - [{author}](https://github.com/{author})

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

> ✨ {author}
'''
"""A template for README.md files (format: 'name', 'author', 'class_name', 'translatepy_repo')"""

SOURCE_README_TEMPLATE = '''\
# {name}

The core implementation for the {name} translator.
'''
"""A template for the source's README.md files (format: 'name')"""

PYPROJECT_TEMPLATE = '''\
[tool.poetry]
name = "{name}"
version = "1.0rc1"
description = "translatepy implementation for {name}"
license = "MIT License"
authors = ["{author}"]
maintainers = ["{author}"]
readme = "README.md"
repository = "https://github.com/{author}/{name}"
documentation = "https://github.com/{author}/{name}/blob/main/README.md"
keywords = [
    "language",
    "translatepy",
    "{name}",
]
classifiers = [
    # Status
    "Development Status :: 4 - Beta",

    # Environment
    "Environment :: Console",

    # Audience
    "Intended Audience :: Developers",

    # Licensing
    "License :: OSI Approved :: MIT License",

    # Software Requirements
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",

    # Topics
    "Topic :: Software Development :: Localization",
    "Topic :: Text Processing",
    "Topic :: Text Processing :: Linguistic",

    # Code quality
    "Typing :: Typed",
]

[tool.poetry.dependencies]
python = "^3.10"
translatepy = "^3.0"

[tool.poetry.urls]
"Issue Tracker" = "https://github.com/{author}/{name}/issues"

[tool.poetry.group.dev.dependencies]
mypy = "^1.4.1"
autopep8 = "^2.0.2"
isort = "^5.12"
pytest = "^7.4"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
'''
"""A template for pyproject.toml files (format: 'author', 'name')"""

LICENSE_TEMPLATE = '''\
Copyright © {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
"""A template for LICENSE files (format: 'year', 'author')"""

GITIGNORE_TEMPLATE = '''\
# This is a file containing different patterns of filenames
# for `git` to ignore. This ranges from cache files to session
# files and build files.


# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# macOS
.DS_Store

# translatepy translate service session files
.translatepy/*

# Nuitka temp files
*.build
*.dist
*.onefile-build
'''
"""A template for .gitignore files"""
