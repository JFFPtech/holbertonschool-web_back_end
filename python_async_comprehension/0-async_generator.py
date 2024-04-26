#!/usr/bin/env python3
""" Async basics, random tasks """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ Yields a random number between 0 and 10 every second for 10 seconds"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
