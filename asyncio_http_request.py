import logging
import asyncio
import time
import requests

from constants import URLS, PROCESS_RUNNING_PER_TIME
from asyncio import Semaphore
from log_utils import format_logging

sem = Semaphore(PROCESS_RUNNING_PER_TIME)


async def get_all_urls():
    """Get URLS using asyncio and requests, limited by the semaphore"""
    async with sem:
        format_logging()
        # Getting loop event from asyncio. Necessary to make 'requests.get' function
        # 'awaitable' more above
        loop = asyncio.get_event_loop()
        for url in URLS:
            print("\n")
            logging.debug(f"Loading {url}")
            # Necessary because 'requests.get' is not 'awaitable'
            future = loop.run_in_executor(None, requests.get, url)
            response = await future
            logging.debug(f"{url} is loaded!")
            # Printing out the response content(influences the performance)
            # print(f"{response.content}")


def main():
    format_logging()
    logging.debug(f"Running all requests using asyncio")
    # Start time counter
    start = time.perf_counter()
    # Starting the main loop
    asyncio.run(get_all_urls())
    # End time counter
    end = time.perf_counter()
    # Total requests time spent
    time_spent = end - start
    logging.debug(f"Time spent for all requests using asyncio: {time_spent: .2f}")


if __name__ == '__main__':
    main()

