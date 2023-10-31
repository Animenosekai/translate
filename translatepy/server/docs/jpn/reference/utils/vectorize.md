# *module* **vectorize**

> [Source: ../../../../../utils/vectorize.py](../../../../../utils/vectorize.py#L0)

Handles vectors

## Imports

- [../../../../../utils/sanitize.py](../../../../../utils/sanitize.py): As `sanitize`

## *const* [**CLEANUP_REGEX**](../../../../../utils/vectorize.py#L12)

## *func* [**string_preprocessing**](../../../../../utils/vectorize.py#L15-L17)

internal function to preprocess the given string for fuzzy search

### Parameters

- **string**: `str`


### Returns

- `str`

## *class* [**Vector**](../../../../../utils/vectorize.py#L20-L34)

A string vector

### *attr* [Vector.**id**](../../../../../utils/vectorize.py#L22)

> Type: `str`

### *attr* [Vector.**string**](../../../../../utils/vectorize.py#L23)

> Type: `str`

### *attr* [Vector.**value**](../../../../../utils/vectorize.py#L24)

> Type: `float`

### *property* [Vector.**counter**](../../../../../utils/vectorize.py#L27-L29)

Returns a counter for the vector

### *property* [Vector.**set**](../../../../../utils/vectorize.py#L32-L34)

Returns a set for the vector

## *const* [**A**](../../../../../utils/vectorize.py#L36)

## *func* [**vectorize**](../../../../../utils/vectorize.py#L38-L45)

Vectorizes the given string

### Parameters

- **id**: `str`


- **string**: `str`


## *class* [**SearchResult**](../../../../../utils/vectorize.py#L49-L54)

A result from the `search` function

### *attr* [SearchResult.**vector**](../../../../../utils/vectorize.py#L51)

> Type: `Vector`

The actual vector

### *attr* [SearchResult.**similarity**](../../../../../utils/vectorize.py#L53)

> Type: `float`

The similarity with the search query

## *func* [**search**](../../../../../utils/vectorize.py#L57-L70)

Searches `query` through `data`

### Parameters

- **data**: `list`


- **query**: `str`


### Returns

- `list`
