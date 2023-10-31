# *module* **request**

> [Source: ../../../../translatepy/utils/request.py @ line 0](../../../../translatepy/utils/request.py#L0)

utils/request  
Extending python requests functionalities with translatepy's own implementation of proxies, caching, exceptions, etc.

## Imports

- [../../../../translatepy/utils/hasher.py](../../../../translatepy/utils/hasher.py): As `hasher`

## Copyright

- **Animenosekai**
Original author
## *const* **RequestHash**

> [Source: ../../../../translatepy/utils/request.py @ line 24](../../../../translatepy/utils/request.py#L24)

## *const* **RateLimitLock**

> [Source: ../../../../translatepy/utils/request.py @ line 27](../../../../translatepy/utils/request.py#L27)

## *const* **CacheLock**

> [Source: ../../../../translatepy/utils/request.py @ line 28](../../../../translatepy/utils/request.py#L28)

## *class* **Session**

> [Source: ../../../../translatepy/utils/request.py @ line 32-225](../../../../translatepy/utils/request.py#L32-L225)

### Raises

- `exceptions.RateLimitPrevention`

### *func* Session.**set_http_proxy**

> [Source: ../../../../translatepy/utils/request.py @ line 52-64](../../../../translatepy/utils/request.py#L52-L64)

Sets the HTTP proxy to use.

#### Parameters

- **proxy**: `str`
  - The HTTP proxy to use.


### *func* Session.**add_http_proxy**

> [Source: ../../../../translatepy/utils/request.py @ line 66-75](../../../../translatepy/utils/request.py#L66-L75)

Adds a HTTP proxy to the list of proxies to use.

#### Parameters

- **proxy**: `str`
  - The HTTP proxy to add.


### *func* Session.**request**

> [Source: ../../../../translatepy/utils/request.py @ line 77-215](../../../../translatepy/utils/request.py#L77-L215)

Make an HTTP request with the provided method.

#### Parameters

- **allow_redirects**: `bool`
  - Default Value: `True`
  - If the request should be allowed to redirect.


- **auth**
  - This value is **optional**
  - An authentication tuple or callable to enable Basic/Digest/Custom HTTP Auth.


- **cache**: `bool`
  - This value is **optional**
  - If the response should be cached.
When None, it will only be cached when the method is in the default_cache_methods attribute.
Note: The response will only be cached if its code is less than 400.


- **cache_duration**: `int`
  - This value is **optional**
  - The duration in seconds the response should be cached.
If None, the default_cache_duration attribute will be used.


- **cert**
  - This value is **optional**
  - A tuple of client cert and key, which will be used if present.


- **cookies**: `dict`
  - This value is **optional**
  - A dictionary of cookies to send.


- **data**
  - This value is **optional**
  - The data to send


- **files**
  - This value is **optional**
  - A dictionary of files to send.


- **headers**: `dict`
  - This value is **optional**
  - A dictionary of HTTP headers to send.


- **hooks**
  - This value is **optional**
  - A dictionary of callables, which if not None, will be called for each


- **invalidate**: `list`, `typing.List[RequestHash]`
  - This value is **optional**
  - A list of requests to invalidate.


- **json**
  - This value is **optional**
  - A JSON serializable Python object to send.


- **method**: `str`
  - The HTTP method to use


- **params**: `dict`
  - This value is **optional**
  - A dictionary of URL parameters to send.


- **proxies**: `dict`
  - This value is **optional**
  - A dictionary mapping protocol to the URL of the proxy.


- **rotate_proxy**: `bool`
  - Default Value: `True`
  - If the proxy should be rotated.


- **stream**: `bool`
  - Default Value: `True`
  - If the response should be streamed.


- **timeout**: `int`
  - This value is **optional**
  - The timeout in seconds for the request.


- **url**: `str`
  - The URL to request


- **verify**
  - This value is **optional**
  - If the SSL cert should be verified.


#### Returns

- `Response`

- `requests.Response`
    - The Response object.

#### Raises

- `exceptions.RateLimitPrevention`

- `requests.exceptions.ConnectionError`
    - In the event of a network problem (e.g. DNS failure, refused connection, etc)

- `requests.exceptions.HTTPError`
    - In the event of the rare invalid HTTP response

- `requests.exceptions.RequestException`
    - If the request fails.

- `requests.exceptions.Timeout`
    - If the request times out

- `requests.exceptions.TooManyRedirects`
    - If a request exceeds the configured number of maximum redirections

#### Examples

##### Example 1

```python
>>> from translatepy.utils.request import Session
>>> s = Session()
>>> s.get('http://httpbin.org/get')
<Response [200]>
```

### *func* Session.**invalidate**

> [Source: ../../../../translatepy/utils/request.py @ line 217-225](../../../../translatepy/utils/request.py#L217-L225)

Invalidates the given request cache.

#### Parameters

- **hash**: `RequestHash`, `requesthash`


## *const* **SharedSession**

> [Source: ../../../../translatepy/utils/request.py @ line 228](../../../../translatepy/utils/request.py#L228)

## *func* **request**

> [Source: ../../../../translatepy/utils/request.py @ line 231-268](../../../../translatepy/utils/request.py#L231-L268)

Make an HTTP request.

### Parameters

- **allow_redirects**: `bool`
  - Default Value: `True`


- **auth**
  - This value is **optional**


- **cache**: `bool`
  - Default Value: `True`


- **cache_duration**: `int`
  - This value is **optional**


- **cert**
  - This value is **optional**


- **cookies**: `dict`
  - This value is **optional**


- **data**
  - This value is **optional**


- **files**
  - This value is **optional**


- **headers**: `dict`
  - This value is **optional**


- **hooks**
  - This value is **optional**


- **invalidate**: `list`, `typing.List[RequestHash]`
  - This value is **optional**


- **json**
  - This value is **optional**


- **method**: `str`


- **params**: `dict`
  - This value is **optional**


- **proxies**: `dict`
  - This value is **optional**


- **rotate_proxy**: `bool`
  - Default Value: `True`


- **session**: `Session`, `session`
  - Default Value: `SharedSession`


- **stream**: `bool`
  - Default Value: `True`


- **timeout**: `int`
  - This value is **optional**


- **url**: `str`


- **verify**
  - This value is **optional**


### Returns

- `requests.Response`

> **Note**
> Look at Session.request for more information.

## *func* **get**

> [Source: ../../../../translatepy/utils/request.py @ line 271-300](../../../../translatepy/utils/request.py#L271-L300)

Make a GET request.

### Parameters

- **allow_redirects**: `bool`
  - Default Value: `True`


- **auth**
  - This value is **optional**


- **cache**: `bool`
  - Default Value: `True`


- **cache_duration**: `int`
  - This value is **optional**


- **cert**
  - This value is **optional**


- **cookies**: `dict`
  - This value is **optional**


- **data**
  - This value is **optional**


- **files**
  - This value is **optional**


- **headers**: `dict`
  - This value is **optional**


- **hooks**
  - This value is **optional**


- **invalidate**: `list`, `typing.List[RequestHash]`
  - This value is **optional**


- **json**
  - This value is **optional**


- **params**: `dict`
  - This value is **optional**


- **proxies**: `dict`
  - This value is **optional**


- **rotate_proxy**: `bool`
  - Default Value: `True`


- **session**: `Session`, `session`
  - Default Value: `SharedSession`


- **stream**: `bool`
  - Default Value: `True`


- **timeout**: `int`
  - This value is **optional**


- **url**: `str`


- **verify**
  - This value is **optional**


> **Note**
> Look at Session.request for more information.

## *func* **post**

> [Source: ../../../../translatepy/utils/request.py @ line 303-332](../../../../translatepy/utils/request.py#L303-L332)

Make a POST request.

### Parameters

- **allow_redirects**: `bool`
  - Default Value: `True`


- **auth**
  - This value is **optional**


- **cache**: `bool`
  - Default Value: `True`


- **cache_duration**: `int`
  - This value is **optional**


- **cert**
  - This value is **optional**


- **cookies**: `dict`
  - This value is **optional**


- **data**
  - This value is **optional**


- **files**
  - This value is **optional**


- **headers**: `dict`
  - This value is **optional**


- **hooks**
  - This value is **optional**


- **invalidate**: `list`, `typing.List[RequestHash]`
  - This value is **optional**


- **json**
  - This value is **optional**


- **params**: `dict`
  - This value is **optional**


- **proxies**: `dict`
  - This value is **optional**


- **rotate_proxy**: `bool`
  - Default Value: `True`


- **session**: `Session`, `session`
  - Default Value: `SharedSession`


- **stream**: `bool`
  - Default Value: `True`


- **timeout**: `int`
  - This value is **optional**


- **url**: `str`


- **verify**
  - This value is **optional**


> **Note**
> Look at Session.request for more information.

## *func* **put**

> [Source: ../../../../translatepy/utils/request.py @ line 335-364](../../../../translatepy/utils/request.py#L335-L364)

Make a PUT request.

### Parameters

- **allow_redirects**: `bool`
  - Default Value: `True`


- **auth**
  - This value is **optional**


- **cache**: `bool`
  - Default Value: `True`


- **cache_duration**: `int`
  - This value is **optional**


- **cert**
  - This value is **optional**


- **cookies**: `dict`
  - This value is **optional**


- **data**
  - This value is **optional**


- **files**
  - This value is **optional**


- **headers**: `dict`
  - This value is **optional**


- **hooks**
  - This value is **optional**


- **invalidate**: `list`, `typing.List[RequestHash]`
  - This value is **optional**


- **json**
  - This value is **optional**


- **params**: `dict`
  - This value is **optional**


- **proxies**: `dict`
  - This value is **optional**


- **rotate_proxy**: `bool`
  - Default Value: `True`


- **session**: `Session`, `session`
  - Default Value: `SharedSession`


- **stream**: `bool`
  - Default Value: `True`


- **timeout**: `int`
  - This value is **optional**


- **url**: `str`


- **verify**
  - This value is **optional**


> **Note**
> Look at Session.request for more information.

## *func* **patch**

> [Source: ../../../../translatepy/utils/request.py @ line 367-396](../../../../translatepy/utils/request.py#L367-L396)

Make a PATCH request.

### Parameters

- **allow_redirects**: `bool`
  - Default Value: `True`


- **auth**
  - This value is **optional**


- **cache**: `bool`
  - Default Value: `True`


- **cache_duration**: `int`
  - This value is **optional**


- **cert**
  - This value is **optional**


- **cookies**: `dict`
  - This value is **optional**


- **data**
  - This value is **optional**


- **files**
  - This value is **optional**


- **headers**: `dict`
  - This value is **optional**


- **hooks**
  - This value is **optional**


- **invalidate**: `list`, `typing.List[RequestHash]`
  - This value is **optional**


- **json**
  - This value is **optional**


- **params**: `dict`
  - This value is **optional**


- **proxies**: `dict`
  - This value is **optional**


- **rotate_proxy**: `bool`
  - Default Value: `True`


- **session**: `Session`, `session`
  - Default Value: `SharedSession`


- **stream**: `bool`
  - Default Value: `True`


- **timeout**: `int`
  - This value is **optional**


- **url**: `str`


- **verify**
  - This value is **optional**


> **Note**
> Look at Session.request for more information.

## *func* **delete**

> [Source: ../../../../translatepy/utils/request.py @ line 399-428](../../../../translatepy/utils/request.py#L399-L428)

Make a DELETE request.

### Parameters

- **allow_redirects**: `bool`
  - Default Value: `True`


- **auth**
  - This value is **optional**


- **cache**: `bool`
  - Default Value: `True`


- **cache_duration**: `int`
  - This value is **optional**


- **cert**
  - This value is **optional**


- **cookies**: `dict`
  - This value is **optional**


- **data**
  - This value is **optional**


- **files**
  - This value is **optional**


- **headers**: `dict`
  - This value is **optional**


- **hooks**
  - This value is **optional**


- **invalidate**: `list`, `typing.List[RequestHash]`
  - This value is **optional**


- **json**
  - This value is **optional**


- **params**: `dict`
  - This value is **optional**


- **proxies**: `dict`
  - This value is **optional**


- **rotate_proxy**: `bool`
  - Default Value: `True`


- **session**: `Session`, `session`
  - Default Value: `SharedSession`


- **stream**: `bool`
  - Default Value: `True`


- **timeout**: `int`
  - This value is **optional**


- **url**: `str`


- **verify**
  - This value is **optional**


> **Note**
> Look at Session.request for more information.

## *func* **head**

> [Source: ../../../../translatepy/utils/request.py @ line 431-460](../../../../translatepy/utils/request.py#L431-L460)

Make a HEAD request.

### Parameters

- **allow_redirects**: `bool`
  - Default Value: `True`


- **auth**
  - This value is **optional**


- **cache**: `bool`
  - Default Value: `True`


- **cache_duration**: `int`
  - This value is **optional**


- **cert**
  - This value is **optional**


- **cookies**: `dict`
  - This value is **optional**


- **data**
  - This value is **optional**


- **files**
  - This value is **optional**


- **headers**: `dict`
  - This value is **optional**


- **hooks**
  - This value is **optional**


- **invalidate**: `list`, `typing.List[RequestHash]`
  - This value is **optional**


- **json**
  - This value is **optional**


- **params**: `dict`
  - This value is **optional**


- **proxies**: `dict`
  - This value is **optional**


- **rotate_proxy**: `bool`
  - Default Value: `True`


- **session**: `Session`, `session`
  - Default Value: `SharedSession`


- **stream**: `bool`
  - Default Value: `True`


- **timeout**: `int`
  - This value is **optional**


- **url**: `str`


- **verify**
  - This value is **optional**


> **Note**
> Look at Session.request for more information.

## *func* **options**

> [Source: ../../../../translatepy/utils/request.py @ line 463-492](../../../../translatepy/utils/request.py#L463-L492)

Make an OPTIONS request.

### Parameters

- **allow_redirects**: `bool`
  - Default Value: `True`


- **auth**
  - This value is **optional**


- **cache**: `bool`
  - Default Value: `True`


- **cache_duration**: `int`
  - This value is **optional**


- **cert**
  - This value is **optional**


- **cookies**: `dict`
  - This value is **optional**


- **data**
  - This value is **optional**


- **files**
  - This value is **optional**


- **headers**: `dict`
  - This value is **optional**


- **hooks**
  - This value is **optional**


- **invalidate**: `list`, `typing.List[RequestHash]`
  - This value is **optional**


- **json**
  - This value is **optional**


- **params**: `dict`
  - This value is **optional**


- **proxies**: `dict`
  - This value is **optional**


- **rotate_proxy**: `bool`
  - Default Value: `True`


- **session**: `Session`, `session`
  - Default Value: `SharedSession`


- **stream**: `bool`
  - Default Value: `True`


- **timeout**: `int`
  - This value is **optional**


- **url**: `str`


- **verify**
  - This value is **optional**


> **Note**
> Look at Session.request for more information.
