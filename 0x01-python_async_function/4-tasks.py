#!/usr/bin/env python3
"""module docs"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function docs"""
    res = []
    delay = [task_wait_random(max_delay) for _ in range(n)]
    for sort in asyncio.as_completed(delay):
        val = await sort
        res.append(val)
    return res
