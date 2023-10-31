# *module* **hasher**

> [Source: ../../../../translatepy/utils/hasher.py](../../../../translatepy/utils/hasher.py#L0)

utils/hasher.py  
Utility to hash different kind of objects

## *func* [**sha256**](../../../../translatepy/utils/hasher.py#L11-L28)

Hashes the given content using SHA-256 and returns its hexadecimal version

### Parameters

- **content**: `bytes`, `str`
  - The content to hash


### Returns

- `str`
    - The SHA-256 hash

## *func* [**hash_object**](../../../../translatepy/utils/hasher.py#L31-L48)

Hashes a given object

### Parameters

- **obj**: `Any`, `typing.Any`


### Returns

- `str`
    - The hash of the object

## *func* [**hash_request**](../../../../translatepy/utils/hasher.py#L51-L82)

Hashes the given request.

### Parameters

- **auth**
  - This value is **optional**


- **cookies**: `NoneType`, `None`, `dict`
  - This value is **optional**


- **data**
  - This value is **optional**


- **files**
  - This value is **optional**


- **headers**: `NoneType`, `None`, `dict`
  - This value is **optional**


- **method**: `str`


- **params**: `NoneType`, `None`, `dict`
  - This value is **optional**


- **url**: `str`


### Returns

- `str`
    - The hash of the request
