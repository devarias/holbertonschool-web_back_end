#!/usr/bin/env python3
"""module doc"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[None, Any]:
    """function docs"""
    if lst:
        return lst[0]
    else:
        return None
