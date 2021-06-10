import requests
import pyuseragents


class Request():
    def __init__(self, proxy_urls={}):
        header = {
            "User-Agent": pyuseragents.random(),
            "Accept": "*/*",
            "Accept-Language": "en-US,en; q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; application/json; charset=UTF-8",
            "Connection": "keep-alive"
        }
        self.session = requests.Session()
        self.header = header
        self.proxies = proxy_urls

    def post(self, url, **kwargs):
        result = self.session.post(url, **kwargs)
        # result.encoding = 'utf-8'
        return result

    def get(self, url, **kwargs):
        result = self.session.get(url, **kwargs)
        # result.encoding = 'utf-8'
        return result

    @property
    def proxies(self):
        return self.session.proxies

    @proxies.setter
    def proxies(self, proxy_urls):
        self.session.proxies = proxy_urls

    @property
    def header(self):
        return self.session.headers

    @header.setter
    def header(self, header_key_value):
        for key, value in header_key_value.items():
            if value is None:
                self.session.headers.pop(key)
            else:
                self.session.headers.update(header_key_value)

    def __del__(self):
        self.session.close()
