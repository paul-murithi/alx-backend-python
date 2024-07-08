#!/usr/bin/env python3
""" Asynchronous coroutine that takes in an integer argument"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Args:
          max_delay: maximum delay

          Return: (float) random delay
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay
