import logging
import asyncio
import time

from random import randint
from asyncio import Semaphore
from constants import LOG_DATETIME_FMT, LOG_FMT_STR, LOG_LEVEL, PROCESS_RUNNING_PER_TIME


# Controls tasks per time through a generator
sem = Semaphore(PROCESS_RUNNING_PER_TIME)


def format_logging():
    """Configures the logging instance"""
    logging.basicConfig(format=LOG_FMT_STR, level=LOG_LEVEL, datefmt=LOG_DATETIME_FMT)


def get_processes():
    """Simulates a getter function which returns a list of process ids"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


async def execute_process(process_id):
    """Executes processes limiting the amount per time using a semaphore"""
    # Forcing log setup inside the concurrent process
    format_logging()
    # Starting a async block code using a Semaphore generator
    async with sem:
        logging.debug(f"Executing process{str(process_id)}")
        # Starting time counter
        start = time.perf_counter()
        # Simulating the process
        await asyncio.sleep(randint(1, 10))
        # Ending time counter
        end = time.perf_counter()
        # Calculating the time spent for a particular processing
        time_spend = end - start
        logging.debug(f"Process{str(process_id)} executed! Time spend: {time_spend:.2f} sec")


async def execute_all():
    """Executes all process by gathering all tasks based on the processes list"""
    # Getting the processes list
    processes = get_processes()
    tasks = []
    # Creating the asynchronous tasks
    [tasks.append(asyncio.create_task(execute_process(p))) for p in processes]
    # Starting tasks concurrently
    await asyncio.gather(*tasks)


async def main():
    # Forcing log format out of concurrent processing
    format_logging()
    logging.debug("Running all processes using asyncio")
    # Start time counter
    start = time.perf_counter()
    # Getting all processes and execute them
    await execute_all()
    # End time counter
    end = time.perf_counter()
    # All processing time spent
    time_spent = end - start
    logging.debug(f"All process using asyncio finished! Time spent: {time_spent: .2f}")


if __name__ == '__main__':
    # Starting the main loop
    asyncio.run(main())
