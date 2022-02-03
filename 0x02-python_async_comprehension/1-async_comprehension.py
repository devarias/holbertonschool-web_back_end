#!/usr/bin/env python3
"""module docs"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function docs"""
    return [i async for i in async_generator()]
