#!/usr/bin/env python3
""" The basics of async """
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio 
async def wait_n(n, max_delay):
    delays = []
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    for result in results:
        delays.append(result)
    return sorted(delays)