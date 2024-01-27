import logging
from constants import LOG_DATETIME_FMT, LOG_FMT_STR, LOG_LEVEL


def format_logging():
    """Configures the logging instance"""
    logging.basicConfig(format=LOG_FMT_STR, level=LOG_LEVEL, datefmt=LOG_DATETIME_FMT)
