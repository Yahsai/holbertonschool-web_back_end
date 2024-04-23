#!/usr/bin/env python3
"""Create a async function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random number between 0 and max delay"""
    ranNum = random.uniform(0, max_delay)
    await asyncio.sleep(ranNum)
    return ranNum
