# plugins

A translatepy implementation of plugins

[![PyPI version](https://badge.fury.io/py/plugins.svg)](https://pypi.org/project/plugins/)
[![Downloads](https://static.pepy.tech/personalized-badge/plugins?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/plugins)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/plugins)](https://pypistats.org/packages/plugins)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/plugins)](https://pypi.org/project/plugins/)
[![PyPI - Status](https://img.shields.io/pypi/status/plugins)](https://pypi.org/project/plugins/)
[![GitHub - License](https://img.shields.io/github/license/Animenosekai/plugins)](https://github.com/Animenosekai/plugins/blob/master/LICENSE)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Animenosekai/plugins)](https://github.com/Animenosekai/plugins)
[![CodeQL Checks Badge](https://github.com/Animenosekai/plugins/workflows/CodeQL%20Python%20Analysis/badge.svg)](https://github.com/Animenosekai/plugins/actions?query=workflow%3ACodeQL)
[![Pytest](https://github.com/Animenosekai/plugins/actions/workflows/pytest.yml/badge.svg)](https://github.com/Animenosekai/plugins/actions/workflows/pytest.yml)
![Code Size](https://img.shields.io/github/languages/code-size/Animenosekai/plugins)
![Repo Size](https://img.shields.io/github/repo-size/Animenosekai/plugins)
![Issues](https://img.shields.io/github/issues/Animenosekai/plugins)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need Python 3 to use this module

```bash
# vermin output
Minimum required versions: 3.8
Incompatible versions:     2
```

Always check if your Python version works with `plugins` before using it in production

## Installing

### Option 1: From PyPI

```bash
pip install --upgrade plugins
```

### Option 2: From Git

```bash
pip install --upgrade git+https://github.com/Animenosekai/plugins
```

You can check if you successfully installed it by printing out its version:

```bash
$ python -c "import plugins; print(plugins.__version__)"
# output:
1.0
```

## Usage

### Directly

You can use it directly as a translator:

```python
>>> from plugins import Plugins
>>> t = Plugins()
>>> t.translate("Hello world", "Japanese")
```

### In a translator aggregator

But you can also use it in a translator aggregator:

```python
>>> from plugins import Plugins
>>> from translatepy import Translator
>>> from translatepy.translators import GoogleTranslate, DeeplTranslate, YandexTranslate
>>> t = Translator([Plugins, GoogleTranslate, DeeplTranslate, YandexTranslate])
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

- [translatepy](https://github.com/Animenosekai/translate)

## Authors

- **Animenosekai** - *Initial work* - [Animenosekai](https://github.com/Animenosekai)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

> ✨ Animenosekai
