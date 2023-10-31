# *module* **DeepL**

> [Source: ../../../../translatepy/translators/DeepL.py](../../../../translatepy/translators/DeepL.py#L0)

DeepL Implementation for translatepy

## Imports

- [../../../../translatepy/translators/base.py](../../../../translatepy/translators/base.py): As `BaseTranslateException`, `BaseTranslator`, `C`

- [../../../../translatepy/translators/base_aggregator.py](../../../../translatepy/translators/base_aggregator.py): As `BaseTranslatorAggregator`

## Copyright

- **Marocco2**
Original implementation
Refer to Animenosekai/translate#7
- **Animenosekai**
Arrangements, optimizations
- **ZhymabekRoman**
Co-Author
## *const* [**SENTENCES_SPLITTING_REGEX**](../../../../translatepy/translators/DeepL.py#L31)

## *class* [**DeeplFormality**](../../../../translatepy/translators/DeepL.py#L34-L36)

### *attr* [DeeplFormality.**formal**](../../../../translatepy/translators/DeepL.py#L35)

### *attr* [DeeplFormality.**informal**](../../../../translatepy/translators/DeepL.py#L36)

## *class* [**DeeplTranslate**](../../../../translatepy/translators/DeepL.py#L39-L41)

## *class* [**DeeplTranslateException**](../../../../translatepy/translators/DeepL.py#L44-L51)

Default DeepL Translate exception

### *attr* [DeeplTranslateException.**error_codes**](../../../../translatepy/translators/DeepL.py#L49)

## *class* [**GetClientState**](../../../../translatepy/translators/DeepL.py#L54-L82)

DeepL Translate state manager

### *func* [GetClientState.**dump**](../../../../translatepy/translators/DeepL.py#L63-L74)

#### Returns

- `dict`

### *func* [GetClientState.**get**](../../../../translatepy/translators/DeepL.py#L76-L82)

Returns a new Client State ID

#### Returns

- `int`

## *class* [**JSONRPCRequest**](../../../../translatepy/translators/DeepL.py#L85-L121)

JSON RPC Request Sender for DeepL

### *func* [JSONRPCRequest.**dump**](../../../../translatepy/translators/DeepL.py#L99-L107)

#### Parameters

- **method**: `str`


- **params**: `dict`


### *func* [JSONRPCRequest.**send_jsonrpc**](../../../../translatepy/translators/DeepL.py#L109-L121)

#### Parameters

- **method**: `str`


- **params**: `dict`


#### Returns

- `dict`

## *class* [**DeeplTranslateV1**](../../../../translatepy/translators/DeepL.py#L124-L308)

### Raises

- `exceptions.UnsupportedMethod`

## *class* [**DeeplTranslateV2**](../../../../translatepy/translators/DeepL.py#L311-L386)

### Raises

- `DeeplTranslateException`
