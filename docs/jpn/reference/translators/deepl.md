# *module* **DeepL**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 0](../../../../translatepy/translators/DeepL.py#L0)

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
## *const* **SENTENCES_SPLITTING_REGEX**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 31](../../../../translatepy/translators/DeepL.py#L31)

## *class* **DeeplFormality**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 34-36](../../../../translatepy/translators/DeepL.py#L34-L36)

### *attr* DeeplFormality.**formal**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 35](../../../../translatepy/translators/DeepL.py#L35)

### *attr* DeeplFormality.**informal**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 36](../../../../translatepy/translators/DeepL.py#L36)

## *class* **DeeplTranslate**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 39-41](../../../../translatepy/translators/DeepL.py#L39-L41)

## *class* **DeeplTranslateException**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 44-51](../../../../translatepy/translators/DeepL.py#L44-L51)

Default DeepL Translate exception

### *attr* DeeplTranslateException.**error_codes**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 49](../../../../translatepy/translators/DeepL.py#L49)

## *class* **GetClientState**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 54-82](../../../../translatepy/translators/DeepL.py#L54-L82)

DeepL Translate state manager

### *func* GetClientState.**dump**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 63-74](../../../../translatepy/translators/DeepL.py#L63-L74)

#### Returns

- `dict`

### *func* GetClientState.**get**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 76-82](../../../../translatepy/translators/DeepL.py#L76-L82)

Returns a new Client State ID

#### Returns

- `int`

## *class* **JSONRPCRequest**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 85-121](../../../../translatepy/translators/DeepL.py#L85-L121)

JSON RPC Request Sender for DeepL

### *func* JSONRPCRequest.**dump**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 99-107](../../../../translatepy/translators/DeepL.py#L99-L107)

#### Parameters

- **method**: `str`


- **params**: `dict`


### *func* JSONRPCRequest.**send_jsonrpc**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 109-121](../../../../translatepy/translators/DeepL.py#L109-L121)

#### Parameters

- **method**: `str`


- **params**: `dict`


#### Returns

- `dict`

## *class* **DeeplTranslateV1**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 124-308](../../../../translatepy/translators/DeepL.py#L124-L308)

### Raises

- `exceptions.UnsupportedMethod`

## *class* **DeeplTranslateV2**

> [Source: ../../../../translatepy/translators/DeepL.py @ line 311-386](../../../../translatepy/translators/DeepL.py#L311-L386)

### Raises

- `DeeplTranslateException`
