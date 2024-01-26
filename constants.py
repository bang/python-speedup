"""
    constants.py

        All constants for the scripts

    Usage example:

        from constants import DATETIME_FMT

        dt_format = DATETIME_FMT
"""


# Formatting log CONSTANTS
DATETIME_FMT = "%Y-%m-%d %H:%M:%S"
FMT_STR = "%(asctime)s [%(levelname)s] - %(message)s"
LOG_LEVEL = 'DEBUG'

# Running config
PROCESS_RUNNING_PER_TIME = 3