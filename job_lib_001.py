import logging
from time import sleep, perf_counter
from joblib import Parallel, delayed, Memory
from constants import DATETIME_FMT, FMT_STR, LOG_LEVEL, PROCESS_RUNNING_PER_TIME


def format_logging():
    """Creates a basic config for log using constants in 'constants.py' file"""
    logging.basicConfig(format=FMT_STR, level=LOG_LEVEL, datefmt=DATETIME_FMT)


def run_process(process_id):
    """Simulates a process running"""
    # It needs to be imported here because random is affected by global context
    from random import randint
    # Setup log inside a job
    format_logging()
    # Start time counter
    start = perf_counter()
    logging.debug(f"Running process {str(process_id)}")
    # Processing simulation
    sleep(randint(1, 10))
    # End time counter
    end = perf_counter()
    # Process(job) time spent
    time_spend = end - start
    logging.debug(f"Process {str(process_id)} is finished! Time spend: {time_spend: .2f} second(s)")


def get_processes():
    """Returns a list with fake processes list"""
    return [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


def process_all():
    """Parallelize all processes running"""
    # Getting process ids list
    process_ids_list = get_processes()
    # Starting a parallel jobs for 'run_process' function
    Parallel(n_jobs=PROCESS_RUNNING_PER_TIME)(
        delayed(run_process)(item) for item in process_ids_list
    )


def main():
    # Setup log
    format_logging()
    logging.debug("Running all process using joblib")
    # Start time counter
    start = perf_counter()
    # Getting processes list and run them
    process_all()
    # End time counter
    end = perf_counter()
    # Total process time spent
    time_spent = end - start
    logging.debug(f"Time spent of all processes: {time_spent: .2f} second(s)")


if __name__ == '__main__':
    main()
