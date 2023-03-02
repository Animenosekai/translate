"""
utils/hasher.py

Utility to hash different kind of objects
"""
import json
import typing
import hashlib


def sha256(content: typing.Union[str, bytes]) -> str:
    """
    Hashes the given content using SHA-256 and returns its hexadecimal version

    Parameters
    ----------
    content: bytes | str
        The content to hash

    Returns
    -------
    str
        The SHA-256 hash
    """
    try:
        return hashlib.sha256(content.encode()).hexdigest()
    except AttributeError:
        return hashlib.sha256(content).hexdigest()


def hash_object(obj: typing.Any) -> str:
    """
    Hashes a given object

    Parameters
    ----------
    obj: typing.Any

    Returns
    -------
    str
        The hash of the object
    """
    try:
        content = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(',', ':'))
    except Exception:
        content = str(obj)
    return sha256(content)


def hash_request(method: str, url: str, params: typing.Optional[dict] = None, data=None, headers: typing.Optional[dict] = None, cookies: typing.Optional[dict] = None, files=None, auth=None) -> str:
    """
    Hashes the given request.

    Parameters
    ----------
    method: str
    url: str
    params: typing.Optional[dict] | dict, default = None
    data: default = None
    headers: typing.Optional[dict] | dict, default = None
    cookies: typing.Optional[dict] | dict, default = None
    files: default = None
    auth: default = None

    Returns
    -------
    str
        The hash of the request
    """

    result = "{url}{method}{params}{data}{headers}{cookies}{files}{auth}".format(
        url=str(url),
        method=str(method).upper().replace(" ", ""),
        params=hash_object(params),
        data=hash_object(data),
        headers=hash_object(headers),
        cookies=hash_object(cookies),
        files=hash_object(files),
        auth=hash_object(auth)
    )
    return sha256(result)
