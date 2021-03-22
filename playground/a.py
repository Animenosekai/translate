# heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c

import json

src = ""
data = ""
resp = ""

post_data = json.dumps([[
    [
        'MkEWBc',
        json.dumps([["text", "src", "destination", True],[None]], separators=(',', ':')),
        None,
        'generic',
    ],
]], separators=(',', ':'))


# broken json parsing
for line in data.split('\n'):
    token_found = token_found or '"MkEWBc"' in line[:30]
    if not token_found:
        continue

    opened_square_bracket = 0
    closed_square_bracket = 0

    is_in_string = False
    for index, char in enumerate(line):
        if char == '\"' and line[max(0, index - 1)] != '\\':
            is_in_string = not is_in_string # flip the bool value
        if not is_in_string:
            if char == '[':
                opened_square_bracket += 1
            elif char == ']':
                closed_square_bracket += 1

    resp += line
    if opened_square_bracket == closed_square_bracket:
        break

# retrieving the info

parsed = json.loads(json.loads(resp)[0][2])
translated = (' ' if parsed[1][0][0][3] else '').join([part[0] for part in parsed[1][0][0][5]])

if src == 'auto':
    try:
        src = parsed[2]
    except: pass

if src == 'auto':
    try:
        src = parsed[0][2]
    except: pass

origin_pronunciation = None
try:
    origin_pronunciation = parsed[0][0]
except: pass

pronunciation = None
try:
    pronunciation = parsed[1][0][0][1]
except: pass
