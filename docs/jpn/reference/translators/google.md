# *module* **Google**

> [Source: ../../../../translatepy/translators/Google.py @ line 0](../../../../translatepy/translators/Google.py#L0)

Google Translate  
This both uses the mobile version of Google Translate, extension endpoints and the `batchexecute` (JSONRPC) API  
The `batchexecute` implementation is heavily inspired by ssut/py-googletrans#255 and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c

## Imports

- [../../../../translatepy/translators/base.py](../../../../translatepy/translators/base.py): As `BaseTranslator`, `C`

- [../../../../translatepy/translators/base_aggregator.py](../../../../translatepy/translators/base_aggregator.py): As `BaseTranslatorAggregator`

## *const* **DOMAINS**

> [Source: ../../../../translatepy/translators/Google.py @ line 21](../../../../translatepy/translators/Google.py#L21)

## *const* **SUPPORTED_LANGUAGES**

> [Source: ../../../../translatepy/translators/Google.py @ line 58](../../../../translatepy/translators/Google.py#L58)

## *class* **GoogleTranslate**

> [Source: ../../../../translatepy/translators/Google.py @ line 66-81](../../../../translatepy/translators/Google.py#L66-L81)

An aggregation of Google Translate translators

### Raises

- `ServiceURLError`

## *class* **GoogleTranslateV1**

> [Source: ../../../../translatepy/translators/Google.py @ line 84-261](../../../../translatepy/translators/Google.py#L84-L261)

A Python implementation of Google Translate's JSONRPC API

### Raises

- `ValueError`

## *class* **GoogleTranslateV2**

> [Source: ../../../../translatepy/translators/Google.py @ line 264-423](../../../../translatepy/translators/Google.py#L264-L423)

A Python implementation of Google Translate's APIs
