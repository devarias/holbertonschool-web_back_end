#!/usr/bin/env python3
"""module docs"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function docs"""
    delay = []
    for _ in range(n):
        delay.append(await wait_random(max_delay))
    return [i for i in sorted(delay)]
