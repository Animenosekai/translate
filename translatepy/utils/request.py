"""
utils/request

Extending python requests functionalities with translatepy's own implementation of proxies, caching, exceptions, etc.

Copyright
---------
Animenosekai
    Original author
"""

import threading
import time
import typing

import pyuseragents
import requests
from requests import HTTPError, PreparedRequest, Request, Response

from translatepy import exceptions
from translatepy.utils import hasher

# Type alias
RequestHash = str

# Locks
RateLimitLock = threading.Lock()
CacheLock = threading.Lock()


# Note this comes from another of my project
class Session(requests.Session):
    def __init__(self) -> None:
        """
        Initializes a new Session object

        A Session lets you keep cookies, settings, cache throughout your requests.

        Returns
        -------
        None
        """
        super().__init__()
        self.cache = {}
        self.default_cache_duration = 3
        self.default_cache_methods = {"GET"}
        self.proxies_list = []
        self.proxies_list_index = 0

        self.rate_limiting_loop_prevention = {}

    def set_http_proxy(self, proxy: str):
        """
        Sets the HTTP proxy to use.

        Parameters
        ----------
        proxy: str
            The HTTP proxy to use.
        """
        self.proxies.update({
            "http": proxy,
            "https": proxy
        })

    def add_http_proxy(self, proxy: str):
        """
        Adds a HTTP proxy to the list of proxies to use.

        Parameters
        ----------
        proxy: str
            The HTTP proxy to add.
        """
        self.proxies_list.append(proxy)

    def request(self, method: str, url: str, cache: bool = None, cache_duration: int = None, invalidate: typing.List[RequestHash] = None, params: dict = None, data=None, headers: dict = None, cookies: dict = None, files=None, auth=None, timeout: int = None, allow_redirects: bool = True, proxies: dict = None, hooks=None, stream: bool = False, verify=None, cert=None, json=None, rotate_proxy: bool = True) -> requests.Response:
        """
        Make an HTTP request with the provided method.

        Example
        -------
        >>> from translatepy.utils.request import Session
        >>> s = Session()
        >>> s.get('http://httpbin.org/get')
        <Response [200]>

        Parameters
        ----------
        method: str
            The HTTP method to use
        url: str
            The URL to request
        cache: bool, default = None
            If the response should be cached.
            When None, it will only be cached when the method is in the default_cache_methods attribute.
            Note: The response will only be cached if its code is less than 400.
        cache_duration: int, default = None
            The duration in seconds the response should be cached.
            If None, the default_cache_duration attribute will be used.
        invalidate: list[requesthash] | typing.list[requesthash] | typing.List[RequestHash], default = None
            A list of requests to invalidate.
        params: dict, default = None
            A dictionary of URL parameters to send.
        data: default = None
            The data to send
        headers: dict, default = None
            A dictionary of HTTP headers to send.
        cookies: dict, default = None
            A dictionary of cookies to send.
        files: default = None
            A dictionary of files to send.
        auth: default = None
            An authentication tuple or callable to enable Basic/Digest/Custom HTTP Auth.
        timeout: int, default = None
            The timeout in seconds for the request.
        allow_redirects: bool, default = True
            If the request should be allowed to redirect.
        proxies: dict, default = None
            A dictionary mapping protocol to the URL of the proxy.
        hooks: default = None
            A dictionary of callables, which if not None, will be called for each
        stream: bool, default = False
            If the response should be streamed.
        verify: default = None
            If the SSL cert should be verified.
        cert: default = None
            A tuple of client cert and key, which will be used if present.
        json: default = None
            A JSON serializable Python object to send.
        rotate_proxy: bool, default = True
            If the proxy should be rotated.

        Returns
        -------
        requests.Response
            The Response object.

        Raises
        ------
        requests.exceptions.ConnectionError
            In the event of a network problem (e.g. DNS failure, refused connection, etc)
        requests.exceptions.HTTPError
            In the event of the rare invalid HTTP response
        requests.exceptions.Timeout
            If the request times out
        requests.exceptions.TooManyRedirects
            If a request exceeds the configured number of maximum redirections
        requests.exceptions.RequestException
            If the request fails.
        """
        # "Making a request to", url
        request_hash = hasher.hash_request(method, url, params, data, headers, cookies, files, auth)

        with RateLimitLock:
            try:
                rate_limiting_data = self.rate_limiting_loop_prevention[request_hash]
            except Exception:
                rate_limiting_data = {
                    "current": 0,
                    "time": time.time_ns()
                }
            if time.time_ns() - rate_limiting_data["time"] < 1e9:
                if rate_limiting_data["current"] > 10:
                    raise exceptions.RateLimitPrevention
            else:
                try:
                    del self.rate_limiting_loop_prevention[request_hash]
                except Exception:
                    pass
            self.rate_limiting_loop_prevention[request_hash] = {
                "time": rate_limiting_data["time"],
                "current": rate_limiting_data["current"] + 1
            }

        with CacheLock:
            current_cache = self.cache.get(request_hash, None)
            if current_cache is not None:
                if time.time() - current_cache["time"] < (cache_duration if cache_duration is not None else self.default_cache_duration):
                    return current_cache["result"]
                else:
                    self.invalidate(request_hash)

        proxies_list_length = len(self.proxies_list)
        if proxies_list_length > 0:
            if rotate_proxy:
                self.proxies_list_index = (self.proxies_list_index + 1) % proxies_list_length
            self.set_http_proxy(self.proxies_list[self.proxies_list_index])

        # Adding a random User-Agent header
        if headers:
            for key in headers:
                key = str(key).lower()
                if key == "user-agent":
                    break
            else:
                headers["User-Agent"] = pyuseragents.random()

        result = super().request(method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)

        # result.raise_for_status = self.overwrite_raise_for_status(result, request_hash=request_hash)

        if result.ok:
            if cache is None:
                if str(method).upper().replace(" ", "") in self.default_cache_methods:
                    cache = True
            if cache:
                self.cache[request_hash] = {
                    "time": time.time(),
                    "result": result
                }
            if invalidate is not None:
                for h in invalidate:
                    self.invalidate(h)
        return result

    def invalidate(self, hash: RequestHash):
        """
        Invalidates the given request cache.

        Parameters
        ----------
        hash: RequestHash | requesthash
        """
        return self.cache.pop(hash, None)


SharedSession = Session()


def request(method: str, url: str, cache: bool = True, cache_duration: int = None, invalidate: typing.List[RequestHash] = None, params: dict = None, data=None, headers: dict = None, cookies: dict = None, files=None, auth=None, timeout: int = None, allow_redirects: bool = True, proxies: dict = None, hooks=None, stream: bool = False, verify=None, cert=None, json=None, rotate_proxy: bool = True, session: Session = SharedSession) -> requests.Response:
    """
    Make an HTTP request.

    Note: Look at Session.request for more information.

    Parameters
    ----------
    method: str
    url: str
    cache: bool, default = True
    cache_duration: int, default = None
    invalidate: typing.list[requesthash] | typing.List[RequestHash], default = None
    params: dict, default = None
    data: default = None
    headers: dict, default = None
    cookies: dict, default = None
    files: default = None
    auth: default = None
    timeout: int, default = None
    allow_redirects: bool, default = True
    proxies: dict, default = None
    hooks: default = None
    stream: bool, default = False
    verify: default = None
    cert: default = None
    json: default = None
    session: session | Session, default = SharedSession
    rotate_proxy: bool, default = True

    Returns
    -------
    requests.Response
    """
    if session is not None:
        return session.request(method, url, cache, cache_duration, invalidate, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json, rotate_proxy)
    with Session() as s:
        return s.request(method, url, cache, cache_duration, invalidate, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json, rotate_proxy)


def get(url: str, cache: bool = True, cache_duration: int = None, invalidate: typing.List[RequestHash] = None, params: dict = None, data=None, headers: dict = None, cookies: dict = None, files=None, auth=None, timeout: int = None, allow_redirects: bool = True, proxies: dict = None, hooks=None, stream: bool = False, verify=None, cert=None, json=None, rotate_proxy: bool = True, session: Session = SharedSession):
    """
    Make a GET request.

    Note: Look at Session.request for more information.

    Parameters
    ----------
    url: str
    cache: bool, default = True
    cache_duration: int, default = None
    invalidate: typing.list[requesthash] | typing.List[RequestHash], default = None
    params: dict, default = None
    data: default = None
    headers: dict, default = None
    cookies: dict, default = None
    files: default = None
    auth: default = None
    timeout: int, default = None
    allow_redirects: bool, default = True
    proxies: dict, default = None
    hooks: default = None
    stream: bool, default = False
    verify: default = None
    cert: default = None
    json: default = None
    session: session | Session, default = SharedSession
    rotate_proxy: bool, default = True
    """
    return request("GET", url, cache, cache_duration, invalidate, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json, rotate_proxy, session)


def post(url: str, cache: bool = True, cache_duration: int = None, invalidate: typing.List[RequestHash] = None, params: dict = None, data=None, headers: dict = None, cookies: dict = None, files=None, auth=None, timeout: int = None, allow_redirects: bool = True, proxies: dict = None, hooks=None, stream: bool = False, verify=None, cert=None, json=None, rotate_proxy: bool = True, session: Session = SharedSession):
    """
    Make a POST request.

    Note: Look at Session.request for more information.

    Parameters
    ----------
    url: str
    cache: bool, default = True
    cache_duration: int, default = None
    invalidate: typing.list[requesthash] | typing.List[RequestHash], default = None
    params: dict, default = None
    data: default = None
    headers: dict, default = None
    cookies: dict, default = None
    files: default = None
    auth: default = None
    timeout: int, default = None
    allow_redirects: bool, default = True
    proxies: dict, default = None
    hooks: default = None
    stream: bool, default = False
    verify: default = None
    cert: default = None
    json: default = None
    session: session | Session, default = SharedSession
    rotate_proxy: bool, default = True
    """
    return request("POST", url, cache, cache_duration, invalidate, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json, rotate_proxy, session)


def put(url: str, cache: bool = True, cache_duration: int = None, invalidate: typing.List[RequestHash] = None, params: dict = None, data=None, headers: dict = None, cookies: dict = None, files=None, auth=None, timeout: int = None, allow_redirects: bool = True, proxies: dict = None, hooks=None, stream: bool = False, verify=None, cert=None, json=None, rotate_proxy: bool = True, session: Session = SharedSession):
    """
    Make a PUT request.

    Note: Look at Session.request for more information.

    Parameters
    ----------
    url: str
    cache: bool, default = True
    cache_duration: int, default = None
    invalidate: typing.list[requesthash] | typing.List[RequestHash], default = None
    params: dict, default = None
    data: default = None
    headers: dict, default = None
    cookies: dict, default = None
    files: default = None
    auth: default = None
    timeout: int, default = None
    allow_redirects: bool, default = True
    proxies: dict, default = None
    hooks: default = None
    stream: bool, default = False
    verify: default = None
    cert: default = None
    json: default = None
    session: session | Session, default = SharedSession
    rotate_proxy: bool, default = True
    """
    return request("PUT", url, cache, cache_duration, invalidate, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json, rotate_proxy, session)


def patch(url: str, cache: bool = True, cache_duration: int = None, invalidate: typing.List[RequestHash] = None, params: dict = None, data=None, headers: dict = None, cookies: dict = None, files=None, auth=None, timeout: int = None, allow_redirects: bool = True, proxies: dict = None, hooks=None, stream: bool = False, verify=None, cert=None, json=None, rotate_proxy: bool = True, session: Session = SharedSession):
    """
    Make a PATCH request.

    Note: Look at Session.request for more information.

    Parameters
    ----------
    url: str
    cache: bool, default = True
    cache_duration: int, default = None
    invalidate: typing.list[requesthash] | typing.List[RequestHash], default = None
    params: dict, default = None
    data: default = None
    headers: dict, default = None
    cookies: dict, default = None
    files: default = None
    auth: default = None
    timeout: int, default = None
    allow_redirects: bool, default = True
    proxies: dict, default = None
    hooks: default = None
    stream: bool, default = False
    verify: default = None
    cert: default = None
    json: default = None
    session: session | Session, default = SharedSession
    rotate_proxy: bool, default = True
    """
    return request("PATCH", url, cache, cache_duration, invalidate, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json, rotate_proxy, session)


def delete(url: str, cache: bool = True, cache_duration: int = None, invalidate: typing.List[RequestHash] = None, params: dict = None, data=None, headers: dict = None, cookies: dict = None, files=None, auth=None, timeout: int = None, allow_redirects: bool = True, proxies: dict = None, hooks=None, stream: bool = False, verify=None, cert=None, json=None, rotate_proxy: bool = True, session: Session = SharedSession):
    """
    Make a DELETE request.

    Note: Look at Session.request for more information.

    Parameters
    ----------
    url: str
    cache: bool, default = True
    cache_duration: int, default = None
    invalidate: typing.list[requesthash] | typing.List[RequestHash], default = None
    params: dict, default = None
    data: default = None
    headers: dict, default = None
    cookies: dict, default = None
    files: default = None
    auth: default = None
    timeout: int, default = None
    allow_redirects: bool, default = True
    proxies: dict, default = None
    hooks: default = None
    stream: bool, default = False
    verify: default = None
    cert: default = None
    json: default = None
    session: session | Session, default = SharedSession
    rotate_proxy: bool, default = True
    """
    return request("DELETE", url, cache, cache_duration, invalidate, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json, rotate_proxy, session)


def head(url: str, cache: bool = True, cache_duration: int = None, invalidate: typing.List[RequestHash] = None, params: dict = None, data=None, headers: dict = None, cookies: dict = None, files=None, auth=None, timeout: int = None, allow_redirects: bool = True, proxies: dict = None, hooks=None, stream: bool = False, verify=None, cert=None, json=None, rotate_proxy: bool = True, session: Session = SharedSession):
    """
    Make a HEAD request.

    Note: Look at Session.request for more information.

    Parameters
    ----------
    url: str
    cache: bool, default = True
    cache_duration: int, default = None
    invalidate: typing.list[requesthash] | typing.List[RequestHash], default = None
    params: dict, default = None
    data: default = None
    headers: dict, default = None
    cookies: dict, default = None
    files: default = None
    auth: default = None
    timeout: int, default = None
    allow_redirects: bool, default = True
    proxies: dict, default = None
    hooks: default = None
    stream: bool, default = False
    verify: default = None
    cert: default = None
    json: default = None
    session: session | Session, default = SharedSession
    rotate_proxy: bool, default = True
    """
    return request("HEAD", url, cache, cache_duration, invalidate, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json, rotate_proxy, session)


def options(url: str, cache: bool = True, cache_duration: int = None, invalidate: typing.List[RequestHash] = None, params: dict = None, data=None, headers: dict = None, cookies: dict = None, files=None, auth=None, timeout: int = None, allow_redirects: bool = True, proxies: dict = None, hooks=None, stream: bool = False, verify=None, cert=None, json=None, rotate_proxy: bool = True, session: Session = SharedSession):
    """
    Make an OPTIONS request.

    Note: Look at Session.request for more information.

    Parameters
    ----------
    url: str
    cache: bool, default = True
    cache_duration: int, default = None
    invalidate: typing.list[requesthash] | typing.List[RequestHash], default = None
    params: dict, default = None
    data: default = None
    headers: dict, default = None
    cookies: dict, default = None
    files: default = None
    auth: default = None
    timeout: int, default = None
    allow_redirects: bool, default = True
    proxies: dict, default = None
    hooks: default = None
    stream: bool, default = False
    verify: default = None
    cert: default = None
    json: default = None
    session: session | Session, default = SharedSession
    rotate_proxy: bool, default = True
    """
    return request("OPTIONS", url, cache, cache_duration, invalidate, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json, rotate_proxy, session)
