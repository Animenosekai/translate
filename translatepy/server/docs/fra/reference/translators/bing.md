# *module* **Bing**

> [Source: ../../../../../translators/Bing.py](../../../../../translators/Bing.py#L0)

This implementation was made specifically for translatepy from 'Zhymabek Roman', based on 'Anime no Sekai' version.

## Imports

- [../../../../../translators/base.py](../../../../../translators/base.py): As `BaseTranslateException`, `BaseTranslator`

## *class* [**BingTranslateException**](../../../../../translators/Bing.py#L20-L23)

### *attr* [BingTranslateException.**error_codes**](../../../../../translators/Bing.py#L21)

## *class* [**BingSessionData**](../../../../../translators/Bing.py#L26-L33)

Bing session data holder

### *attr* [BingSessionData.**ig**](../../../../../translators/Bing.py#L28)

> Type: `str`

### *attr* [BingSessionData.**iid**](../../../../../translators/Bing.py#L29)

> Type: `str`

### *attr* [BingSessionData.**key**](../../../../../translators/Bing.py#L30)

> Type: `cain.types.UInt64`

### *attr* [BingSessionData.**token**](../../../../../translators/Bing.py#L31)

> Type: `str`

### *attr* [BingSessionData.**cookies_keys**](../../../../../translators/Bing.py#L32)

> Type: `List`

### *attr* [BingSessionData.**cookies_values**](../../../../../translators/Bing.py#L33)

> Type: `List`

## *class* [**BingSessionManager**](../../../../../translators/Bing.py#L36-L136)

Creates and manages a Bing session

### Raises

- `BingTranslateException`

### *func* [BingSessionManager.**send**](../../../../../translators/Bing.py#L92-L136)

Sends requestts to the API

#### Parameters

- **data**


- **url**


#### Raises

- `BingTranslateException`

## *class* [**BingTranslate**](../../../../../translators/Bing.py#L145-L251)

A Python implementation of Microsoft Bing Translation's APIs

### Raises

- `BingTranslateException`

- `UnsupportedMethod`
