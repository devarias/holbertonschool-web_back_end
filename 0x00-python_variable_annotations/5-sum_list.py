#!/usr/bin/env python3
"""module doc"""

from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function docs"""
    return reduce(lambda a, b: a+b, input_list)
