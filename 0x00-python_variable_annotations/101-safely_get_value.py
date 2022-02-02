#!/usr/bin/env python3
"""module doc"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[None, T] = None) -> Union[Any, T]:
    """function docs"""
    if key in dct:
        return dct[key]
    else:
        return default
