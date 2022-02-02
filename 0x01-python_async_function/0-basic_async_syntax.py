#!/usr/bin/env python3
"""module docs"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """function docs"""
    sec = random.uniform(0, max_delay)
    await asyncio.sleep(sec)
    return sec
