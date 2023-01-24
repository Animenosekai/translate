from copy import copy
from json import loads
from time import time
from typing import List, Union

import pyuseragents
import requests
from requests.models import CaseInsensitiveDict
from translatepy.exceptions import RequestStatusError
from translatepy.utils.lru import LRUDictCache


class Response():
    def __init__(self, request_obj: requests.Response) -> None:
        #: Integer Code of responded HTTP Status, e.g. 404 or 200.
        self.status_code = request_obj.status_code

        #: Case-insensitive Dictionary of Response Headers.
        #: For example, ``headers['content-encoding']`` will return the
        #: value of a ``'Content-Encoding'`` response header.
        self.headers = request_obj.headers

        #: File-like object representation of response (for advanced usage).
        #: Use of ``raw`` requires that ``stream=True`` be set on the request.
        #: This requirement does not apply for use internally to Requests.
        self.raw = request_obj.raw

        #: Final URL location of Response.
        self.url = request_obj.url

        #: Encoding to decode with when accessing r.text.
        self.encoding = request_obj.encoding

        #: A list of :class:`Response <Response>` objects from
        #: the history of the Request. Any redirect responses will end
        #: up here. The list is sorted from the oldest to the most recent request.
        self.history = request_obj.history

        #: Textual reason of responded HTTP Status, e.g. "Not Found" or "OK".
        self.reason = request_obj.reason

        #: A CookieJar of Cookies the server sent back.
        self.cookies = request_obj.cookies

        #: The amount of time elapsed between sending the request
        #: and the arrival of the response (as a timedelta).
        #: This property specifically measures the time taken between sending
        #: the first byte of the request and finishing parsing the headers. It
        #: is therefore unaffected by consuming the response content or the
        #: value of the ``stream`` keyword argument.
        self.elapsed = request_obj.elapsed

        #: The :class:`PreparedRequest <PreparedRequest>` object to which this
        #: is a response.
        self.request = request_obj.request

        # properties
        self.content = request_obj.content
        self.apparent_encoding = request_obj.apparent_encoding
        self.is_redirect = request_obj.is_redirect
        self.is_permanent_redirect = request_obj.is_permanent_redirect
        self.links = request_obj.links
        self.next = request_obj.next
        self.ok = request_obj.ok

    @property
    def text(self, encoding="utf-8") -> str:
        """Returns the text/str version of the response (decoded)"""
        try:
            return self.content.decode(encoding)
        except Exception:
            return str(self.content).encode(encoding).decode(encoding)

    def raise_for_status(self):
        """Raise an exception if the status code of the response is less than 400"""
        if self.status_code >= 400:
            raise RequestStatusError(self.status_code, "Request Status Code: {code}".format(code=str(self.status_code)))

    def json(self, **kwargs):
        return loads(self.text, **kwargs)


class Request():
    def __init__(self, proxy_urls: Union[str, List] = None, cache_duration: Union[int, float] = 2):
        """
        translatepy's version of `requests.Session`

        It includes caching, headers management and proxy management

        Parameters:
        ----------
            proxy_urls : str | list
                The URL(s) for the proxies to be used (they will be used as HTTP and HTTPS proxies)
            cache_duration : int | float
                The duration of the cache for GET requests

        Returns:
        --------
            Response:
                The response for the request
        """
        HEADERS = {
            "User-Agent": pyuseragents.random(),
            "Accept": "*/*",
            "Accept-Language": "en-US,en-GB; q=0.5",
            "Accept-Encoding": "gzip, deflate",
            # "Content-Type": "application/x-www-form-urlencoded; application/json; charset=UTF-8",
            "Connection": "keep-alive"
        }
# default headers
#        HEADERS = {
#            "User-Agent": "python-requests/2.23.0",
#            "Accept": "*/*",
#            "Accept-Encoding": "gzip, deflate",
#            "Connection": "keep-alive"
#        }
        self.session = requests.Session()

        self.GETCACHE = LRUDictCache()
        self.cache_duration = float(cache_duration)

        self.headers = HEADERS

        self._proxies_index = 0
        self.proxies = ([proxy_urls] if isinstance(proxy_urls, str) else list(proxy_urls) if proxy_urls is not None else [])
        if len(self.proxies) == 0:
            self.proxies = [None]

    def _set_session_proxies(self, url: str = None):
        """Internal function to set the proxies"""
        if url is not None:
            self.session.proxies.update({
                "http": url,
                "https": url
            })

    def post(self, url: str, **kwargs) -> Response:
        """
        Makes a POST request with the given URL

        Parameters:
        ----------
            url : str
                The URL to send a POST request to
            **kwargs : parameters
                This is the options that will be passed to requests.Session.post

        Returns:
        --------
            Response:
                The response for the request
        """
        self._set_session_proxies(self.proxies[self._proxies_index])
        request = self.session.post(url, **kwargs)
        result = Response(request)
        request.close()
        if self._proxies_index != len(self.proxies) - 1:
            self._proxies_index += 1
        else:
            self._proxies_index = 0
        return result

    def get(self, url: str, **kwargs) -> Response:
        """
        Makes a GET request with the given URL

        Parameters:
        ----------
            url : str
                The URL to send a GET request to
            **kwargs : parameters
                This is the options that will be passed to requests.Session.get

        Returns:
        --------
            Response:
                The response for the request
        """
        _cache_key = str(url) + str(kwargs)
        if _cache_key in self.GETCACHE and time() - self.GETCACHE[_cache_key]["timestamp"] < self.cache_duration:
            return self.GETCACHE[_cache_key]["response"]
        self._set_session_proxies(self.proxies[self._proxies_index])
        request = self.session.get(url, **kwargs)
        result = Response(request)
        request.close()
        if self._proxies_index != len(self.proxies) - 1:
            self._proxies_index += 1
        else:
            self._proxies_index = 0
        self.GETCACHE[_cache_key] = {
            "timestamp": time(),
            "response": copy(result)
        }
        return result

    @property
    def headers(self) -> CaseInsensitiveDict:
        """The headers set for the session"""
        return self.session.headers

    @headers.setter
    def headers(self, header_key_value: dict):
        """Setter for the headers"""
        for key, value in header_key_value.items():
            if value is None:
                try:
                    self.session.headers.pop(key)
                except Exception:
                    continue
            else:
                self.session.headers.update(header_key_value)

    def __del__(self):
        """Closing the session"""
        self.session.close()
