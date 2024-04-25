#!/usr/bin/env python3
""" Async Basics """

import asyncio
import random


async def wait_random(max_delay: int = 5) -> float:
    """ Wait for a random delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
