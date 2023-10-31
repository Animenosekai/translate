# *module* **DeepL**

> [Source: ../../../../../translators/DeepL.py @ line 0](../../../../../translators/DeepL.py#L0)

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
## *const* **SENTENCES_SPLITTING_REGEX**

> [Source: ../../../../../translators/DeepL.py @ line 31](../../../../../translators/DeepL.py#L31)

## *class* **DeeplFormality**

> [Source: ../../../../../translators/DeepL.py @ line 34-36](../../../../../translators/DeepL.py#L34-L36)

### *attr* DeeplFormality.**formal**

> [Source: ../../../../../translators/DeepL.py @ line 35](../../../../../translators/DeepL.py#L35)

### *attr* DeeplFormality.**informal**

> [Source: ../../../../../translators/DeepL.py @ line 36](../../../../../translators/DeepL.py#L36)

## *class* **DeeplTranslate**

> [Source: ../../../../../translators/DeepL.py @ line 39-41](../../../../../translators/DeepL.py#L39-L41)

## *class* **DeeplTranslateException**

> [Source: ../../../../../translators/DeepL.py @ line 44-51](../../../../../translators/DeepL.py#L44-L51)

Default DeepL Translate exception

### *attr* DeeplTranslateException.**error_codes**

> [Source: ../../../../../translators/DeepL.py @ line 49](../../../../../translators/DeepL.py#L49)

## *class* **GetClientState**

> [Source: ../../../../../translators/DeepL.py @ line 54-82](../../../../../translators/DeepL.py#L54-L82)

DeepL Translate state manager

### *func* GetClientState.**dump**

> [Source: ../../../../../translators/DeepL.py @ line 63-74](../../../../../translators/DeepL.py#L63-L74)

#### Returns

- `dict`

### *func* GetClientState.**get**

> [Source: ../../../../../translators/DeepL.py @ line 76-82](../../../../../translators/DeepL.py#L76-L82)

Returns a new Client State ID

#### Returns

- `int`

## *class* **JSONRPCRequest**

> [Source: ../../../../../translators/DeepL.py @ line 85-121](../../../../../translators/DeepL.py#L85-L121)

JSON RPC Request Sender for DeepL

### *func* JSONRPCRequest.**dump**

> [Source: ../../../../../translators/DeepL.py @ line 99-107](../../../../../translators/DeepL.py#L99-L107)

#### Parameters

- **method**: `str`


- **params**: `dict`


### *func* JSONRPCRequest.**send_jsonrpc**

> [Source: ../../../../../translators/DeepL.py @ line 109-121](../../../../../translators/DeepL.py#L109-L121)

#### Parameters

- **method**: `str`


- **params**: `dict`


#### Returns

- `dict`

## *class* **DeeplTranslateV1**

> [Source: ../../../../../translators/DeepL.py @ line 124-308](../../../../../translators/DeepL.py#L124-L308)

### Raises

- `exceptions.UnsupportedMethod`

## *class* **DeeplTranslateV2**

> [Source: ../../../../../translators/DeepL.py @ line 311-386](../../../../../translators/DeepL.py#L311-L386)

### Raises

- `DeeplTranslateException`
