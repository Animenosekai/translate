# *module* **importer**

> [Source: ../../../../../utils/importer.py @ line 0](../../../../../utils/importer.py#L0)

importer.py  
A module to allow for dynamic importing of translators.

## Imports

- [../../../../../utils/lru.py](../../../../../utils/lru.py): As `lru`

- [../../../../../utils/vectorize.py](../../../../../utils/vectorize.py): As `vectorize`

## *const* **IMPORTER_CACHE**

> [Source: ../../../../../utils/importer.py @ line 18](../../../../../utils/importer.py#L18)

## *const* **IMPORTER_DATA_DIR**

> [Source: ../../../../../utils/importer.py @ line 20](../../../../../utils/importer.py#L20)

## *const* **IMPORTER_DATA_FILE**

> [Source: ../../../../../utils/importer.py @ line 21](../../../../../utils/importer.py#L21)

## *const* **NAMED_TRANSLATORS**

> [Source: ../../../../../utils/importer.py @ line 27](../../../../../utils/importer.py#L27)

## *func* **translator_from_name**

> [Source: ../../../../../utils/importer.py @ line 37-42](../../../../../utils/importer.py#L37-L42)

Retrieves the given translate from its name

### Parameters

- **name**: `str`


### Returns

- `type`

### Raises

- `ValueError`

## *func* **translator_from_path**

> [Source: ../../../../../utils/importer.py @ line 45-55](../../../../../utils/importer.py#L45-L55)

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

> [Source: ../../../../../utils/importer.py @ line 58-94](../../../../../utils/importer.py#L58-L94)

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
