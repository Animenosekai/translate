"""
Make backward compatible annotations
"""
from sys import version_info

if version_info < (3, 9):
    from typing import Tuple, List, Dict
else:
    List = list
    Tuple = tuple
    Dict = dict