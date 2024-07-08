#!/usr/bin/env python3
""" Coroutine at the same time with async """


import random
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Args:
          max_delay: max wait
          n: spawn function

       Return: (float)  list of all delays
    """
    delays: List[float] = []
    tasks: List = []

    for x in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
