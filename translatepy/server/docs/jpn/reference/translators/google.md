# *module* **Google**

> [Source: ../../../../../translators/Google.py](../../../../../translators/Google.py#L0)

Google Translate  
This both uses the mobile version of Google Translate, extension endpoints and the `batchexecute` (JSONRPC) API  
The `batchexecute` implementation is heavily inspired by ssut/py-googletrans#255 and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c

## Imports

- [../../../../../translators/base.py](../../../../../translators/base.py): As `BaseTranslator`, `C`

- [../../../../../translators/base_aggregator.py](../../../../../translators/base_aggregator.py): As `BaseTranslatorAggregator`

## *const* [**DOMAINS**](../../../../../translators/Google.py#L21)

## *const* [**SUPPORTED_LANGUAGES**](../../../../../translators/Google.py#L58)

## *class* [**GoogleTranslate**](../../../../../translators/Google.py#L66-L81)

An aggregation of Google Translate translators

### Raises

- `ServiceURLError`

## *class* [**GoogleTranslateV1**](../../../../../translators/Google.py#L84-L261)

A Python implementation of Google Translate's JSONRPC API

### Raises

- `ValueError`

## *class* [**GoogleTranslateV2**](../../../../../translators/Google.py#L264-L423)

A Python implementation of Google Translate's APIs
