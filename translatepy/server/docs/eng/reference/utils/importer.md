# *module* **importer**

> [Source: ../../../../../utils/importer.py](../../../../../utils/importer.py#L0)

importer.py  
A module to allow for dynamic importing of translators.

## Imports

- [../../../../../utils/lru.py](../../../../../utils/lru.py): As `lru`

- [../../../../../utils/vectorize.py](../../../../../utils/vectorize.py): As `vectorize`

## *const* [**IMPORTER_CACHE**](../../../../../utils/importer.py#L18)

## *const* [**IMPORTER_DATA_DIR**](../../../../../utils/importer.py#L20)

## *const* [**IMPORTER_DATA_FILE**](../../../../../utils/importer.py#L21)

## *const* [**NAMED_TRANSLATORS**](../../../../../utils/importer.py#L27)

## *func* [**translator_from_name**](../../../../../utils/importer.py#L37-L42)

Retrieves the given translate from its name

### Parameters

- **name**: `str`


### Returns

- `type`

### Raises

- `ValueError`

## *func* [**translator_from_path**](../../../../../utils/importer.py#L45-L55)

Returns a translator from its dot path

### Parameters

- **forceload**: `bool`
  - Default Value: `True`


- **path**: `str`


### Returns

- `type`

### Raises

- `ImportError`

## *func* [**get_translator**](../../../../../utils/importer.py#L58-L94)

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
