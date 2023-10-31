# *module* **lru**

> [Source: ../../../../../utils/lru.py](../../../../../utils/lru.py#L0)

lru.py  
LRU cache implementation for the translatepy project.

## *const* [**logger**](../../../../../utils/lru.py#L16)

## *class* [**LRUDictCache**](../../../../../utils/lru.py#L19-L38)

### *func* [LRUDictCache.**clear**](../../../../../utils/lru.py#L37-L38)

## *class* [**SizeLimitedLRUCache**](../../../../../utils/lru.py#L41-L173)

Special implementation of a size limited LRU cache.

### *func* [SizeLimitedLRUCache.**get_size**](../../../../../utils/lru.py#L135-L170)

Get the size of an object.

#### Parameters

- **builtin**: `bool`
  - Default Value: `True`
  - Whether to use the builtin sys.getsizeof function or not.
This function is faster than the custom implementation but might yield inaccurate results for complex objects.


- **obj**: `Any`
  - The object to get the size of.


#### Returns

- `int`
    - The size of the object in bytes.

> **Note**
> The second implementation of this function is based on the following article:
    https://towardsdatascience.com/the-strange-size-of-python-objects-in-memory-ce87bdfbb97f

### *func* [SizeLimitedLRUCache.**clear**](../../../../../utils/lru.py#L172-L173)

## *func* [**timed_lru_cache**](../../../../../utils/lru.py#L176-L198)

### Parameters

- **maxsize**: `int`
  - Default Value: `128`


- **seconds**: `int`

