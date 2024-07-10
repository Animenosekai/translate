# *module* **Papago**

> [Source: ../../../../../translators/Papago.py](../../../../../translators/Papago.py#L0)

translatepy's implementation of <Papago>

## Imports

- [../../../../../translators/base.py](../../../../../translators/base.py): As `BaseTranslateException`, `BaseTranslator`, `C`

## *class* [**PapagoException**](../../../../../translators/Papago.py#L18-L21)

### *attr* [PapagoException.**error_codes**](../../../../../translators/Papago.py#L19)

## *class* [**PapagoSessionData**](../../../../../translators/Papago.py#L27-L31)

Bing session data holder

### *attr* [PapagoSessionData.**timestamp**](../../../../../translators/Papago.py#L29)

> Type: `cain.types.UInt64`

### *attr* [PapagoSessionData.**cookies_keys**](../../../../../translators/Papago.py#L30)

> Type: `List`

### *attr* [PapagoSessionData.**cookies_values**](../../../../../translators/Papago.py#L31)

> Type: `List`

## *const* [**SESSION_CACHE_EXPIRATION**](../../../../../translators/Papago.py#L34)

## *class* [**Papago**](../../../../../translators/Papago.py#L37-L262)

translatepy's implementation of <Papago>

### Raises

- `ValueError`

- `exceptions.UnsupportedLanguage`

### *func* [Papago.**generate_headers**](../../../../../translators/Papago.py#L83-L119)

Generates the headers for the API

#### Parameters

- **request_id**: `str`


- **url**: `str`


#### Returns

- `dict`
