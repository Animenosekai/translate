"""
Trying to read values from Google's batchexecute
"""
from requests import get, post
from bs4 import BeautifulSoup
from json import loads, dumps
from random import randint
from urllib.parse import urlencode

class BatchExecute():
    def __init__(self) -> None:
        # will be set by _reloadWiz
        self._wiz = None
        self._ui_path = "TranslateWebserverUi"
        self._f_sid = None
        self._bl = None
        # constants
        self._rpcids = "MkEWBc"
        self._hl = "en"
        self._reqid = randint(1000, 9999)
        self._rt = "c"

        self._reloadWiz()

    def _reloadWiz(self):
        request = get("https://translate.google.com/", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}).text
        _wiz = request[request.find("window.WIZ_global_data = ") + 25:request.find(";</script>")]
        _wiz = loads(_wiz)
        self._ui_path = _wiz.get("qwAQke", None)
        self._bl = _wiz.get("cfb2h", None)
        self._f_sid = _wiz.get("FdrFJe", None)

    def _makeParams(self):
        r = {
            "rpcids": self._rpcids,
            "f.sid": self._f_sid,
            "bl": self._bl,
            "hl": self._hl,
            "_reqid": self._reqid,
            "rt": self._rt,
        }
        return urlencode(r)

    def _makeData(self, text, source, destination):
        return f'[[["MkEWBc", "[[\\"{text}\\",\\"{source}\\",\\"{destination}\\",true],[null]]", null,"1"]]]'


    def _makeURL(self):
        return "https://translate.google.com/_/" + self._ui_path + "/data/batchexecute?" + self._makeParams()

    def translate(self, text, source, destination):
        r = post(self._makeURL(), data=self._makeData(text, source, destination), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36', "Content-Type": "application/x-www-form-urlencoded"})
        self._reqid += 100000
        print(r.status_code)
        print(r.text)


b = BatchExecute()
