#!/usr/bin/env python3
"""module doc"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """function docs"""
    return (k, v ** 2)
