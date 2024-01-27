"""
    constants.py

        All constants for the scripts

    Usage example:

        from constants import DATETIME_FMT

        dt_format = DATETIME_FMT
"""


# Formatting log CONSTANTS
LOG_DATETIME_FMT = "%Y-%m-%d %H:%M:%S"
LOG_FMT_STR = "%(asctime)s [%(levelname)s] - %(message)s"
LOG_LEVEL = 'DEBUG'

# Running config
PROCESS_RUNNING_PER_TIME = 5

# HTTP sites
HTTP_SITES = [
    'https://www.google.com', 'https://www.amazon.com', 'https://www.github.com',
    'https://uol.com.br', 'https://www.medium.com', 'https://www.wired.com',
    'https://www.youtube.com', 'https://9gag.com', 'https://www.realpython.com',
    'https://linkedin.com'
]
