# Installation

## Prerequisites

You will need Python 3 to use this module

```bash
# vermin output
Minimum required versions: 3.2
Incompatible versions:     2
```

According to Vermin (`--backport typing`), Python 3.2 is needed for the backport of typing, but some may say that it is available for python versions higher than 3.0

Always check if your Python version works with `translatepy` before using it in production

## Installing

### Option 1: From PyPI

```bash
pip install --upgrade translatepy
```

### Option 2: From Git

```bash
pip install --upgrade git+https://github.com/Animenosekai/translate
```

You can check if you successfully installed it by printing out its version:

```bash
$ translatepy --version
# output:
translatepy v2.3
```

or just:

```bash
$ python -c "import translatepy; print(translatepy.__version__)"
# output:
translatepy v2.3
```
