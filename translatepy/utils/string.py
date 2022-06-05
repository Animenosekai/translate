"""
string.py

Manages string manipulation utilities.
"""


def toCamelCase(string: str):
    """
    Converts a string to camel case

    Parameters
    ----------
        string: str
            The string to convert
    """
    string = str(string)
    if string.isupper():
        return string
    split = string.split("_")  # split by underscore
    final_split = []
    for s in split:
        final_split.extend(s.split(" "))  # split by space
    return "".join(l.capitalize() if index > 0 else l for index, l in enumerate(final_split))
