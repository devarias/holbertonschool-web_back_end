#!/usr/bin/env python3
"""module docs"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function docs"""
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension(),
                           async_comprehension(),
                           async_comprehension(),
                           async_comprehension()))
    e = time.perf_counter() - s
    return e
