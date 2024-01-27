import logging
import asyncio
import time

from random import randint
from asyncio import Semaphore
from constants import DATETIME_FMT, FMT_STR, LOG_LEVEL, PROCESS_RUNNING_PER_TIME


# Controls tasks per time
sem = Semaphore(PROCESS_RUNNING_PER_TIME)


def format_logging():
    """Configures the logging instance"""
    logging.basicConfig(format=FMT_STR, level=LOG_LEVEL, datefmt=DATETIME_FMT)


def get_processes():
    """Simulates a getter function which returns a list of process ids"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


async def execute_process(process_id):
    """Executes processes limiting the amount per time using a semaphore"""
    format_logging()
    # Limiting tasks amount by semaphore parameter using the
    # available generator
    async with sem:
        logging.debug(f"Executing process{str(process_id)}")
        start = time.perf_counter()
        # Simulating the process
        await asyncio.sleep(randint(1, 10))
        end = time.perf_counter()
        time_spend = end - start
        logging.debug(f"Process{str(process_id)} executed! Time spend: {time_spend:.2f} sec")


async def execute_all():
    """Executes all process by gathering all tasks based on the processes list"""
    processes = get_processes()
    tasks = []
    [tasks.append(asyncio.create_task(execute_process(p))) for p in processes]
    await asyncio.gather(*tasks)


async def main():
    format_logging()
    logging.debug("Running all processes using asyncio")
    start = time.perf_counter()
    await execute_all()
    end = time.perf_counter()
    time_spent = end - start
    logging.debug(f"All process using asyncio finished! Time spent: {time_spent: .2f}")


if __name__ == '__main__':
    # Starting the main loop
    asyncio.run(main())
