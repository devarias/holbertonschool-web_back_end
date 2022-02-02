#!/usr/bin/env python3
"""module doc"""

from functools import reduce
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """function docs"""
    return float(reduce(lambda a, b: a + b, mxd_lst))
