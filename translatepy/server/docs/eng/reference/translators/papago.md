# *module* **Papago**

> [Source: ../../../../../translators/Papago.py @ line 0](../../../../../translators/Papago.py#L0)

translatepy's implementation of <Papago>

## Imports

- [../../../../../translators/base.py](../../../../../translators/base.py): As `BaseTranslateException`, `BaseTranslator`, `C`

## *class* **PapagoException**

> [Source: ../../../../../translators/Papago.py @ line 18-21](../../../../../translators/Papago.py#L18-L21)

### *attr* PapagoException.**error_codes**

> [Source: ../../../../../translators/Papago.py @ line 19](../../../../../translators/Papago.py#L19)

## *class* **PapagoSessionData**

> [Source: ../../../../../translators/Papago.py @ line 27-31](../../../../../translators/Papago.py#L27-L31)

Bing session data holder

### *attr* PapagoSessionData.**timestamp**

> [Source: ../../../../../translators/Papago.py @ line 29](../../../../../translators/Papago.py#L29)

> Type: `cain.types.UInt64`

### *attr* PapagoSessionData.**cookies_keys**

> [Source: ../../../../../translators/Papago.py @ line 30](../../../../../translators/Papago.py#L30)

> Type: `List`

### *attr* PapagoSessionData.**cookies_values**

> [Source: ../../../../../translators/Papago.py @ line 31](../../../../../translators/Papago.py#L31)

> Type: `List`

## *const* **SESSION_CACHE_EXPIRATION**

> [Source: ../../../../../translators/Papago.py @ line 34](../../../../../translators/Papago.py#L34)

## *class* **Papago**

> [Source: ../../../../../translators/Papago.py @ line 37-262](../../../../../translators/Papago.py#L37-L262)

translatepy's implementation of <Papago>

### Raises

- `ValueError`

- `exceptions.UnsupportedLanguage`

### *func* Papago.**generate_headers**

> [Source: ../../../../../translators/Papago.py @ line 83-119](../../../../../translators/Papago.py#L83-L119)

Generates the headers for the API

#### Parameters

- **request_id**: `str`


- **url**: `str`


#### Returns

- `dict`
