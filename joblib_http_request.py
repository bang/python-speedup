import logging
import requests
from time import perf_counter
from joblib import Parallel, delayed, Memory
from constants import LOG_DATETIME_FMT, LOG_FMT_STR, LOG_LEVEL, PROCESS_RUNNING_PER_TIME, URLS


def format_logging():
    """Creates a basic config for log using constants in 'constants.py' file"""
    logging.basicConfig(format=LOG_FMT_STR, level=LOG_LEVEL, datefmt=LOG_DATETIME_FMT)


def get_url(url):
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
    """Parallelize all processes running"""
    Parallel(n_jobs=PROCESS_RUNNING_PER_TIME)(
        delayed(get_url)(url) for url in URLS
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
