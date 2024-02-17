import logging
import requests
from time import perf_counter
from joblib import Parallel, delayed
from constants import PROCESS_RUNNING_PER_TIME, URLS
from log_utils import format_logging


def get_all_urls(url):
    """Simulates a process running"""
    # It needs to be imported here because random is affected by global context
    from random import randint
    format_logging()
    start = perf_counter()
    logging.debug(f"Loading URL: {str(url)}")
    # Processing simulation
    requests.get(url)
    end = perf_counter()
    time_spend = end - start
    logging.debug(f"{str(url)} is loaded! Time spend: {time_spend: .2f} second(s)")


def process_all():
    """Parallelize all URL accesses"""
    Parallel(n_jobs=PROCESS_RUNNING_PER_TIME)(
        delayed(get_all_urls)(url) for url in URLS
    )


def main():
    format_logging()
    logging.debug("Running all requests using joblib")
    start = perf_counter()
    process_all()
    end = perf_counter()
    time_spent = end - start
    logging.debug(f"Time spent of all requests: {time_spent: .2f} second(s)")


if __name__ == '__main__':
    main()
