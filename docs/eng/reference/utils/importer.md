# *module* **importer**

> [Source: ../../../../translatepy/utils/importer.py @ line 0](../../../../translatepy/utils/importer.py#L0)

importer.py  
A module to allow for dynamic importing of translators.

## Imports

- [../../../../translatepy/utils/lru.py](../../../../translatepy/utils/lru.py): As `lru`

- [../../../../translatepy/utils/vectorize.py](../../../../translatepy/utils/vectorize.py): As `vectorize`

## *const* **IMPORTER_CACHE**

> [Source: ../../../../translatepy/utils/importer.py @ line 18](../../../../translatepy/utils/importer.py#L18)

## *const* **IMPORTER_DATA_DIR**

> [Source: ../../../../translatepy/utils/importer.py @ line 20](../../../../translatepy/utils/importer.py#L20)

## *const* **IMPORTER_DATA_FILE**

> [Source: ../../../../translatepy/utils/importer.py @ line 21](../../../../translatepy/utils/importer.py#L21)

## *const* **NAMED_TRANSLATORS**

> [Source: ../../../../translatepy/utils/importer.py @ line 27](../../../../translatepy/utils/importer.py#L27)

## *func* **translator_from_name**

> [Source: ../../../../translatepy/utils/importer.py @ line 37-42](../../../../translatepy/utils/importer.py#L37-L42)

Retrieves the given translate from its name

### Parameters

- **name**: `str`


### Returns

- `type`

### Raises

- `ValueError`

## *func* **translator_from_path**

> [Source: ../../../../translatepy/utils/importer.py @ line 45-55](../../../../translatepy/utils/importer.py#L45-L55)

Returns a translator from its dot path

### Parameters

- **forceload**: `bool`
  - Default Value: `True`


- **path**: `str`


### Returns

- `type`

### Raises

- `ImportError`

## *func* **get_translator**

> [Source: ../../../../translatepy/utils/importer.py @ line 58-94](../../../../translatepy/utils/importer.py#L58-L94)

Searches the given translator

### Parameters

- **forceload**: `bool`
  - Default Value: `True`


- **query**: `str`


- **threshold**: `float`
  - Default Value: `90`


### Returns

- `type`

### Raises

- `exceptions.UnknownTranslator`
