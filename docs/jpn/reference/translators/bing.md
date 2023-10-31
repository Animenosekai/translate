# *module* **Bing**

> [Source: ../../../../translatepy/translators/Bing.py @ line 0](../../../../translatepy/translators/Bing.py#L0)

This implementation was made specifically for translatepy from 'Zhymabek Roman', based on 'Anime no Sekai' version.

## Imports

- [../../../../translatepy/translators/base.py](../../../../translatepy/translators/base.py): As `BaseTranslateException`, `BaseTranslator`

## *class* **BingTranslateException**

> [Source: ../../../../translatepy/translators/Bing.py @ line 20-23](../../../../translatepy/translators/Bing.py#L20-L23)

### *attr* BingTranslateException.**error_codes**

> [Source: ../../../../translatepy/translators/Bing.py @ line 21](../../../../translatepy/translators/Bing.py#L21)

## *class* **BingSessionData**

> [Source: ../../../../translatepy/translators/Bing.py @ line 26-33](../../../../translatepy/translators/Bing.py#L26-L33)

Bing session data holder

### *attr* BingSessionData.**ig**

> [Source: ../../../../translatepy/translators/Bing.py @ line 28](../../../../translatepy/translators/Bing.py#L28)

> Type: `str`

### *attr* BingSessionData.**iid**

> [Source: ../../../../translatepy/translators/Bing.py @ line 29](../../../../translatepy/translators/Bing.py#L29)

> Type: `str`

### *attr* BingSessionData.**key**

> [Source: ../../../../translatepy/translators/Bing.py @ line 30](../../../../translatepy/translators/Bing.py#L30)

> Type: `cain.types.UInt64`

### *attr* BingSessionData.**token**

> [Source: ../../../../translatepy/translators/Bing.py @ line 31](../../../../translatepy/translators/Bing.py#L31)

> Type: `str`

### *attr* BingSessionData.**cookies_keys**

> [Source: ../../../../translatepy/translators/Bing.py @ line 32](../../../../translatepy/translators/Bing.py#L32)

> Type: `List`

### *attr* BingSessionData.**cookies_values**

> [Source: ../../../../translatepy/translators/Bing.py @ line 33](../../../../translatepy/translators/Bing.py#L33)

> Type: `List`

## *class* **BingSessionManager**

> [Source: ../../../../translatepy/translators/Bing.py @ line 36-136](../../../../translatepy/translators/Bing.py#L36-L136)

Creates and manages a Bing session

### Raises

- `BingTranslateException`

### *func* BingSessionManager.**send**

> [Source: ../../../../translatepy/translators/Bing.py @ line 92-136](../../../../translatepy/translators/Bing.py#L92-L136)

Sends requestts to the API

#### Parameters

- **data**


- **url**


#### Raises

- `BingTranslateException`

## *class* **BingTranslate**

> [Source: ../../../../translatepy/translators/Bing.py @ line 145-251](../../../../translatepy/translators/Bing.py#L145-L251)

A Python implementation of Microsoft Bing Translation's APIs

### Raises

- `BingTranslateException`

- `UnsupportedMethod`
