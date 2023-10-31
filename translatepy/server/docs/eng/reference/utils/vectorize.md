# *module* **vectorize**

> [Source: ../../../../../utils/vectorize.py @ line 0](../../../../../utils/vectorize.py#L0)

Handles vectors

## Imports

- [../../../../../utils/sanitize.py](../../../../../utils/sanitize.py): As `sanitize`

## *const* **CLEANUP_REGEX**

> [Source: ../../../../../utils/vectorize.py @ line 12](../../../../../utils/vectorize.py#L12)

## *func* **string_preprocessing**

> [Source: ../../../../../utils/vectorize.py @ line 15-17](../../../../../utils/vectorize.py#L15-L17)

internal function to preprocess the given string for fuzzy search

### Parameters

- **string**: `str`


### Returns

- `str`

## *class* **Vector**

> [Source: ../../../../../utils/vectorize.py @ line 20-34](../../../../../utils/vectorize.py#L20-L34)

A string vector

### *attr* Vector.**id**

> [Source: ../../../../../utils/vectorize.py @ line 22](../../../../../utils/vectorize.py#L22)

> Type: `str`

### *attr* Vector.**string**

> [Source: ../../../../../utils/vectorize.py @ line 23](../../../../../utils/vectorize.py#L23)

> Type: `str`

### *attr* Vector.**value**

> [Source: ../../../../../utils/vectorize.py @ line 24](../../../../../utils/vectorize.py#L24)

> Type: `float`

### *property* Vector.**counter**

> [Source: ../../../../../utils/vectorize.py @ line 27-29](../../../../../utils/vectorize.py#L27-L29)

Returns a counter for the vector

### *property* Vector.**set**

> [Source: ../../../../../utils/vectorize.py @ line 32-34](../../../../../utils/vectorize.py#L32-L34)

Returns a set for the vector

## *const* **A**

> [Source: ../../../../../utils/vectorize.py @ line 36](../../../../../utils/vectorize.py#L36)

## *func* **vectorize**

> [Source: ../../../../../utils/vectorize.py @ line 38-45](../../../../../utils/vectorize.py#L38-L45)

Vectorizes the given string

### Parameters

- **id**: `str`


- **string**: `str`


## *class* **SearchResult**

> [Source: ../../../../../utils/vectorize.py @ line 49-54](../../../../../utils/vectorize.py#L49-L54)

A result from the `search` function

### *attr* SearchResult.**vector**

> [Source: ../../../../../utils/vectorize.py @ line 51](../../../../../utils/vectorize.py#L51)

> Type: `Vector`

The actual vector

### *attr* SearchResult.**similarity**

> [Source: ../../../../../utils/vectorize.py @ line 53](../../../../../utils/vectorize.py#L53)

> Type: `float`

The similarity with the search query

## *func* **search**

> [Source: ../../../../../utils/vectorize.py @ line 57-70](../../../../../utils/vectorize.py#L57-L70)

Searches `query` through `data`

### Parameters

- **data**: `list`


- **query**: `str`


### Returns

- `list`
