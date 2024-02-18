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
PROCESS_RUNNING_PER_TIME = 4

URLS = [
    'https://www.google.com',
    'https://www.medium.com',
    'https://www.microsoft.com',
    'https://www.ebay.com',
    'https://www.aws.com',
    'https://www.youtube.com',
    'https://www.netflix.com',
    'https://www.wired.com'
]