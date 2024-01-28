import logging
import time
import requests

from time import perf_counter
from multiprocessing import Pool
from constants import PROCESS_RUNNING_PER_TIME, URLS
from log_utils import format_logging


def get_all_urls(url):
    """Simulates a process running"""
    # It needs to be imported here because random is affected by global context
    from random import randint
    format_logging()
    start = perf_counter()
    logging.debug(f"Loading {str(url)}")
    # Processing simulation
    requests.get(url)
    end = perf_counter()
    time_spend = end - start
    logging.debug(f"{str(url)} loaded! Time spent using multiprocessing: {time_spend: .2f} second(s)")


def main():
    format_logging()
    logging.debug("Running all processes using multiprocessing")
    start = time.perf_counter()
    pool = Pool(PROCESS_RUNNING_PER_TIME)
    pool.map(get_all_urls, URLS)
    end = time.perf_counter()
    time_spent = end - start
    logging.debug(f"All processes ran using multiprocess was finished! Total time spent: {time_spent: .2f}")


if __name__ == '__main__':
    main()
