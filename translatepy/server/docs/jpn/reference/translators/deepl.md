# *module* **DeepL**

> [Source: ../../../../../translators/DeepL.py](../../../../../translators/DeepL.py#L0)

DeepL Implementation for translatepy

## Imports

- [../../../../../translators/base.py](../../../../../translators/base.py): As `BaseTranslateException`, `BaseTranslator`, `C`

- [../../../../../translators/base_aggregator.py](../../../../../translators/base_aggregator.py): As `BaseTranslatorAggregator`

## Copyright

- **Marocco2**
Original implementation
Refer to Animenosekai/translate#7
- **Animenosekai**
Arrangements, optimizations
- **ZhymabekRoman**
Co-Author
## *const* [**SENTENCES_SPLITTING_REGEX**](../../../../../translators/DeepL.py#L31)

## *class* [**DeeplFormality**](../../../../../translators/DeepL.py#L34-L36)

### *attr* [DeeplFormality.**formal**](../../../../../translators/DeepL.py#L35)

### *attr* [DeeplFormality.**informal**](../../../../../translators/DeepL.py#L36)

## *class* [**DeeplTranslate**](../../../../../translators/DeepL.py#L39-L41)

## *class* [**DeeplTranslateException**](../../../../../translators/DeepL.py#L44-L51)

Default DeepL Translate exception

### *attr* [DeeplTranslateException.**error_codes**](../../../../../translators/DeepL.py#L49)

## *class* [**GetClientState**](../../../../../translators/DeepL.py#L54-L82)

DeepL Translate state manager

### *func* [GetClientState.**dump**](../../../../../translators/DeepL.py#L63-L74)

#### Returns

- `dict`

### *func* [GetClientState.**get**](../../../../../translators/DeepL.py#L76-L82)

Returns a new Client State ID

#### Returns

- `int`

## *class* [**JSONRPCRequest**](../../../../../translators/DeepL.py#L85-L121)

JSON RPC Request Sender for DeepL

### *func* [JSONRPCRequest.**dump**](../../../../../translators/DeepL.py#L99-L107)

#### Parameters

- **method**: `str`


- **params**: `dict`


### *func* [JSONRPCRequest.**send_jsonrpc**](../../../../../translators/DeepL.py#L109-L121)

#### Parameters

- **method**: `str`


- **params**: `dict`


#### Returns

- `dict`

## *class* [**DeeplTranslateV1**](../../../../../translators/DeepL.py#L124-L308)

### Raises

- `exceptions.UnsupportedMethod`

## *class* [**DeeplTranslateV2**](../../../../../translators/DeepL.py#L311-L386)

### Raises

- `DeeplTranslateException`
