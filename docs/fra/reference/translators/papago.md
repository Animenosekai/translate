# *module* **Papago**

> [Source: ../../../../translatepy/translators/Papago.py @ line 0](../../../../translatepy/translators/Papago.py#L0)

translatepy's implementation of <Papago>

## Imports

- [../../../../translatepy/translators/base.py](../../../../translatepy/translators/base.py): As `BaseTranslateException`, `BaseTranslator`, `C`

## *class* **PapagoException**

> [Source: ../../../../translatepy/translators/Papago.py @ line 18-21](../../../../translatepy/translators/Papago.py#L18-L21)

### *attr* PapagoException.**error_codes**

> [Source: ../../../../translatepy/translators/Papago.py @ line 19](../../../../translatepy/translators/Papago.py#L19)

## *class* **PapagoSessionData**

> [Source: ../../../../translatepy/translators/Papago.py @ line 27-31](../../../../translatepy/translators/Papago.py#L27-L31)

Bing session data holder

### *attr* PapagoSessionData.**timestamp**

> [Source: ../../../../translatepy/translators/Papago.py @ line 29](../../../../translatepy/translators/Papago.py#L29)

> Type: `cain.types.UInt64`

### *attr* PapagoSessionData.**cookies_keys**

> [Source: ../../../../translatepy/translators/Papago.py @ line 30](../../../../translatepy/translators/Papago.py#L30)

> Type: `List`

### *attr* PapagoSessionData.**cookies_values**

> [Source: ../../../../translatepy/translators/Papago.py @ line 31](../../../../translatepy/translators/Papago.py#L31)

> Type: `List`

## *const* **SESSION_CACHE_EXPIRATION**

> [Source: ../../../../translatepy/translators/Papago.py @ line 34](../../../../translatepy/translators/Papago.py#L34)

## *class* **Papago**

> [Source: ../../../../translatepy/translators/Papago.py @ line 37-262](../../../../translatepy/translators/Papago.py#L37-L262)

translatepy's implementation of <Papago>

### Raises

- `ValueError`

- `exceptions.UnsupportedLanguage`

### *func* Papago.**generate_headers**

> [Source: ../../../../translatepy/translators/Papago.py @ line 83-119](../../../../translatepy/translators/Papago.py#L83-L119)

Generates the headers for the API

#### Parameters

- **request_id**: `str`


- **url**: `str`


#### Returns

- `dict`
