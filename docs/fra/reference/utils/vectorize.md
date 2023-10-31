# *module* **vectorize**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 0](../../../../translatepy/utils/vectorize.py#L0)

Handles vectors

## Imports

- [../../../../translatepy/utils/sanitize.py](../../../../translatepy/utils/sanitize.py): As `sanitize`

## *const* **CLEANUP_REGEX**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 12](../../../../translatepy/utils/vectorize.py#L12)

## *func* **string_preprocessing**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 15-17](../../../../translatepy/utils/vectorize.py#L15-L17)

internal function to preprocess the given string for fuzzy search

### Parameters

- **string**: `str`


### Returns

- `str`

## *class* **Vector**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 20-34](../../../../translatepy/utils/vectorize.py#L20-L34)

A string vector

### *attr* Vector.**id**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 22](../../../../translatepy/utils/vectorize.py#L22)

> Type: `str`

### *attr* Vector.**string**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 23](../../../../translatepy/utils/vectorize.py#L23)

> Type: `str`

### *attr* Vector.**value**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 24](../../../../translatepy/utils/vectorize.py#L24)

> Type: `float`

### *property* Vector.**counter**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 27-29](../../../../translatepy/utils/vectorize.py#L27-L29)

Returns a counter for the vector

### *property* Vector.**set**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 32-34](../../../../translatepy/utils/vectorize.py#L32-L34)

Returns a set for the vector

## *const* **A**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 36](../../../../translatepy/utils/vectorize.py#L36)

## *func* **vectorize**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 38-45](../../../../translatepy/utils/vectorize.py#L38-L45)

Vectorizes the given string

### Parameters

- **id**: `str`


- **string**: `str`


## *class* **SearchResult**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 49-54](../../../../translatepy/utils/vectorize.py#L49-L54)

A result from the `search` function

### *attr* SearchResult.**vector**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 51](../../../../translatepy/utils/vectorize.py#L51)

> Type: `Vector`

The actual vector

### *attr* SearchResult.**similarity**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 53](../../../../translatepy/utils/vectorize.py#L53)

> Type: `float`

The similarity with the search query

## *func* **search**

> [Source: ../../../../translatepy/utils/vectorize.py @ line 57-70](../../../../translatepy/utils/vectorize.py#L57-L70)

Searches `query` through `data`

### Parameters

- **data**: `list`


- **query**: `str`


### Returns

- `list`
