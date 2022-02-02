#!/usr/bin/env python3
"""module docs"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int,  max_delay: int) -> List[float]:
    """function docs"""
    done, process = [], []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(
            lambda future_obj: done.append(future_obj.result()))
        process.append(task)
    await asyncio.gather(*process)
    return done
