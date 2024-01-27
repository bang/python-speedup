import logging
import time
from time import sleep, perf_counter
from multiprocessing import Pool
from constants import DATETIME_FMT, FMT_STR, LOG_LEVEL, PROCESS_RUNNING_PER_TIME


def format_logging():
    """Creates a basic config for log using constants in 'constants.py' file"""
    logging.basicConfig(format=FMT_STR, level=LOG_LEVEL, datefmt=DATETIME_FMT)


def run_process(process_id):
    """Simulates a process running"""
    # It needs to be imported here because random is affected by global context
    from random import randint
    format_logging()
    start = perf_counter()
    logging.debug(f"Running process {str(process_id)}")
    # Processing simulation
    sleep(randint(1, 10))
    end = perf_counter()
    time_spend = end - start
    logging.debug(f"Process {str(process_id)} is finished! Time spend: {time_spend: .2f} second(s)")


def get_processes():
    """Returns a list with fake processes list"""
    return [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


def main():
    format_logging()
    logging.debug("Running all processes using multiprocessing")
    start = time.perf_counter()
    # Pool with processes per time limited by the constant
    pool = Pool(PROCESS_RUNNING_PER_TIME)
    pool.map(run_process, get_processes())
    end = time.perf_counter()
    time_spent = end - start
    logging.debug(f"All processes ran using multiprocess was finished! Total time spent: {time_spent: .2f}")


if __name__ == '__main__':
    main()
