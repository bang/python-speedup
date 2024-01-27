import logging
import asyncio
import time

import requests

from constants import LOG_FMT_STR, LOG_DATETIME_FMT, LOG_LEVEL, URLS, PROCESS_RUNNING_PER_TIME
from asyncio import Semaphore
from log_utils import format_logging

sem = Semaphore(PROCESS_RUNNING_PER_TIME)


async def get_urls():
    """Get URLS using asyncio and requests, limited by the semaphore"""
    async with sem:
        format_logging()
        loop = asyncio.get_event_loop()
        for url in URLS:
            print("\n")
            logging.debug(f"Loading {url}")
            future = loop.run_in_executor(None, requests.get, url)
            response = await future
            logging.debug(f"{url} is loaded!")
            # Do something with response


def main():
    format_logging()
    logging.debug(f"Running all requests using asyncio")
    start = time.perf_counter()
    asyncio.run(get_urls())
    end = time.perf_counter()
    time_spent = end - start
    logging.debug(f"Time spent for all requests using asyncio: {time_spent: .2f}")


if __name__ == '__main__':
    main()

