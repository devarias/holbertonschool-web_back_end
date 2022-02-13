#!/usr/bin/env python3
""" module docs """
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ method docs """
    for item in fields:
        message = re.sub(fr'{item}=.+?{separator}',
                         f'{item}={redaction}{separator}', message)
    return message
