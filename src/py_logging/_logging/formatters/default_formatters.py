from __future__ import annotations

import logging

DEFAULT_LOG_FORMATTER: dict = {
    "default": {
        "format": "[%(asctime)s] [%(levelname)s] > [%(filename)s:%(lineno)d] [%(funcName)s]: %(message)s",
        "datefmt": "%Y-%m-%d %H:%M:%S",
    }
}

DEFAULT_LOG_CONSOLE_HANLDER: dict = {
    "default_console_handler": {
        "class": "logging.StreamHandler",
        "formatter": "default",
        "level": "DEBUG",
        "stream": "ext://sys.stdout",
    }
}

DEFAULT_REQUESTS_LOGGER: dict = {"level": "WARNING"}

DEFAULT_ROOT_LOGGER: dict = {
    "handlers": ["default_console_handler"],
    "level": "DEBUG",
}
