# Source: en.wikipedia.org/wiki/Whitespace_character
# Note: BRAILLE PATTERN BLANK, HANGUL FILLER, HANGUL CHOSEONG FILLER, HANGUL JUNGSEONG FILLER and HALFWIDTH HANGUL FILLER are also refered here as "whitespaces" while they aren't according to the Unicode standard.
WHITESPACES = ["\u0009", "\u000A", "\u000B", "\u000C", "\u000D", "\u0020", "\u0085", "\u00A0", "\u1680", "\u2000", "\u2001", "\u2002", "\u2003", "\u2004", "\u2005", "\u2006", "\u2007", "\u2008", "\u2009", "\u200A", "\u2028", "\u2029", "\u202F", "\u205F", "\u3000", "\u180E", "\u200B",
               "\u200C", "\u200D", "\u2060", "\uFEFF", "\u00B7", "\u21A1", "\u2261", "\u237D", "\u23CE", "\u2409", "\u240A", "\u240B", "\u240C", "\u240D", "\u2420", "\u2422", "\u2423", "\u2424", "\u25B3", "\u2A5B", "\u2AAA", "\u2AAB", "\u3037", "\u2800", "\u3164", "\u115F", "\u1160", "\uFFA0"]

WHITESPACES += ["\u000A", "\u000D"] # \n, \r

def remove_spaces(string: str):
    """Removes all whitespaces from the given string"""
    if string is None:
        return ""
    string = str(string)
    for char in WHITESPACES:
        string = string.replace(char, "")
    return string
