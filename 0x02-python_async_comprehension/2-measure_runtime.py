#!/usr/bin/env python3
""" Measure times """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime coroutine executes async_comprehension four times in
    parallel using asyncio.gather.

    Return: (float) random numbers
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start_time

    return (elapsed)
