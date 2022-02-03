#!/usr/bin/env python3
"""module docs"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function docs"""
    delay: List[float] = []
    all: List[float] = []
    for i in range(n):
        delay.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delay):
        earliest_result = await delay
        all.append(earliest_result)
    return all
