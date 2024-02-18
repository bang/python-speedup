import logging
import requests
from time import perf_counter
from joblib import Parallel, delayed
from constants import PROCESS_RUNNING_PER_TIME, URLS
from log_utils import format_logging


def get_all_urls(url):
    """Simulates a process running"""
    # Setup log for each job
    format_logging()
    # Start time counter
    start = perf_counter()
    logging.debug(f"Loading URL: {str(url)}")
    # Processing simulation
    requests.get(url)
    # End time counter
    end = perf_counter()
    # Total single request time spent
    time_spend = end - start
    logging.debug(f"{str(url)} request is finished! Time spend: {time_spend: .2f} second(s)")


def process_all():
    """Parallelize all URL requests"""
    Parallel(n_jobs=PROCESS_RUNNING_PER_TIME)(
        delayed(get_all_urls)(url) for url in URLS
    )


def main():
    # Setup log
    format_logging()
    logging.debug("Running all requests using joblib")
    # Start time counter
    start = perf_counter()
    # Performing all HTTP requests
    process_all()
    # End time counter
    end = perf_counter()
    # Total requests time spent
    time_spent = end - start
    logging.debug(f"Time spent of all requests: {time_spent: .2f} second(s)")


if __name__ == '__main__':
    main()
