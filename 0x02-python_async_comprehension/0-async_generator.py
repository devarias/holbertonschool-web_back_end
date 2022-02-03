#!/usr/bin/env python3
"""module docs"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """function docs"""
    n: int = 10
    for i in range(n):
        await asyncio.sleep(1)
        yield random.uniform(0, n)
