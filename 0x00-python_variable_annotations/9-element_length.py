#!/usr/bin/env python3
"""module doc"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function docs"""
    return [(i, len(i)) for i in lst]
