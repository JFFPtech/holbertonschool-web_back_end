#!/usr/bin/env python3
""" Async basics, concurrent coroutines """

import asyncio
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns list of delays