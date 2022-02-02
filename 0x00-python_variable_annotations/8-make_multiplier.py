#!/usr/bin/env python3
"""module doc"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function docs"""
    return lambda x: x * multiplier
