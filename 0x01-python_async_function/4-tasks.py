#!/usr/bin/env python3
"""module docs"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int,  max_delay: int) -> List[float]:
    """function docs"""
    done, process = [], []
    for _ in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(
            lambda future_obj: done.append(future_obj.result()))
        process.append(task)
    await asyncio.gather(*process)
    return done
