## Initialize app logger high up in the package heirarchy to ensure child loggers
#  instantiated with logging.getLogger(__name__) inherit defaults from the root logger.
from __future__ import annotations

import logging
from logging.config import dictConfig

from py_logging._logging import DEFAULT_LOGGING_CONFIG

dictConfig(DEFAULT_LOGGING_CONFIG)
logging.getLogger(__name__).addHandler(logging.NullHandler())
