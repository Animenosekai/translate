# heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
from json import loads, dumps

from requests import post

def _request(text, destination, source):
    """
    Makes a translation request to Google Translate RPC API
    """
    rpc_request = dumps([[
        [
            'MkEWBc',
            dumps([[str(text), str(destination), str(source), True],[None]], separators=(',', ':')),
            None,
            'generic',
        ],
    ]], separators=(',', ':'))
    data = {
        "f.req": rpc_request
    }
    params = {
        'rpcids': "MkEWBc",
        'bl': 'boq_translate-webserver_20201207.13_p0',
        'soc-app': 1,
        'soc-platform': 1,
        'soc-device': 1,
        'rt': 'c',
    }
    request = post('https://translate.google.com/_/TranslateWebserverUi/data/batchexecute', params=params, data=data)
    if request.status_code < 400:
        return request.text
    return None

def _parse_response(data):
    """
    Parses the broken JSON response given by the new RPC API endpoint (batchexecute)
    """
    token_found = False
    resp = ""
    opening_bracket = 0
    closing_bracket = 0
    # broken json parsing
    for line in data.split('\n'):
        token_found = token_found or '"MkEWBc"' in line[:30]
        if not token_found:
            continue

        is_in_string = False
        for index, char in enumerate(line):
            if char == '\"' and line[max(0, index - 1)] != '\\':
                is_in_string = not is_in_string
            if not is_in_string:
                if char == '[':
                    opening_bracket += 1
                elif char == ']':
                    closing_bracket += 1

        resp += line
        if opening_bracket == closing_bracket:
            break

    return loads(loads(resp)[0][2])

def translate(text, destination_language, source_language):
    request = _request(text, destination_language, source_language)    
    parsed = _parse_response(request)
    translated = (' ' if parsed[1][0][0][3] else '').join([part[0] for part in parsed[1][0][0][5]])

    source_language = str(source_language)
    try:
        source_language = parsed[2]
    except Exception: pass

    if source_language.lower() == 'auto':
        try:
            source_language = parsed[0][2]
        except Exception: pass

    if source_language == 'auto' or source_language is None:
        try:
            source_language = parsed[0][1][1][0]
        except Exception: pass

    return source_language, translated

def transliterate(text, source_language):
    request = _request(text, "en", source_language)    
    parsed = _parse_response(request)

    source_language = str(source_language)
    try:
        source_language = parsed[2]
    except Exception: pass

    if source_language.lower() == 'auto':
        try:
            source_language = parsed[0][2]
        except Exception: pass

    if source_language == 'auto' or source_language is None:
        try:
            source_language = parsed[0][1][1][0]
        except Exception: pass

    origin_pronunciation = None
    try:
        origin_pronunciation = parsed[0][0]
    except Exception: pass

    return source_language, origin_pronunciation

def language(text):
    request = _request(text, "en", "auto")    
    parsed = _parse_response(request)

    source_language = None
    try:
        source_language = parsed[2]
    except Exception: pass

    if source_language == 'auto' or source_language is None:
        try:
            source_language = parsed[0][2]
        except Exception: pass

    if source_language == 'auto' or source_language is None:
        try:
            source_language = parsed[0][1][1][0]
        except Exception: pass

    return source_language
