from re import compile

POSITIVE_FLOAT_REGEX = compile("[^0-9.]")


def convert_to_float(element) -> float:
    """
    Safely converts anything to a positive float
    """
    element = POSITIVE_FLOAT_REGEX.sub("", str(element))
    if element != '':
        return float(element)
    return float(0)
