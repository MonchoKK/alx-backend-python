#!/usr/bin/env python3
"""
A module that measures the time it takes to run
a number of asynchromious task at a time
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time it takes to run `wait_n` with `n` coroutines
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n