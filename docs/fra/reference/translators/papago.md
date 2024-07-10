# *module* **Papago**

> [Source: ../../../../translatepy/translators/Papago.py](../../../../translatepy/translators/Papago.py#L0)

translatepy's implementation of <Papago>

## Imports

- [../../../../translatepy/translators/base.py](../../../../translatepy/translators/base.py): As `BaseTranslateException`, `BaseTranslator`, `C`

## *class* [**PapagoException**](../../../../translatepy/translators/Papago.py#L18-L21)

### *attr* [PapagoException.**error_codes**](../../../../translatepy/translators/Papago.py#L19)

## *class* [**PapagoSessionData**](../../../../translatepy/translators/Papago.py#L27-L31)

Bing session data holder

### *attr* [PapagoSessionData.**timestamp**](../../../../translatepy/translators/Papago.py#L29)

> Type: `cain.types.UInt64`

### *attr* [PapagoSessionData.**cookies_keys**](../../../../translatepy/translators/Papago.py#L30)

> Type: `List`

### *attr* [PapagoSessionData.**cookies_values**](../../../../translatepy/translators/Papago.py#L31)

> Type: `List`

## *const* [**SESSION_CACHE_EXPIRATION**](../../../../translatepy/translators/Papago.py#L34)

## *class* [**Papago**](../../../../translatepy/translators/Papago.py#L37-L262)

translatepy's implementation of <Papago>

### Raises

- `ValueError`

- `exceptions.UnsupportedLanguage`

### *func* [Papago.**generate_headers**](../../../../translatepy/translators/Papago.py#L83-L119)

Generates the headers for the API

#### Parameters

- **request_id**: `str`


- **url**: `str`


#### Returns

- `dict`
