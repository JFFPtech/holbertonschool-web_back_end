#!/usr/bin/python3
""" Async Basics """

import asyncio
import random

async def wait_random(max_delay: int = 5) -> float:
    """ Wait for a random delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    results = await asyncio.gather(
        wait_random(),  # Uses default max_delay of 5
        wait_random(10), # Different max_delay of 10
        wait_random(3)  # Different max_delay of 3
    )
    for result in results:
        print(f"Waited for {result:.2f} seconds.")

# Execute the main function within the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
