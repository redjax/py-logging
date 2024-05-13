from __future__ import annotations

from .formatters import (
    DEFAULT_LOG_CONSOLE_HANLDER,
    DEFAULT_LOG_FORMATTER,
    DEFAULT_ROOT_LOGGER,
)

DEFAULT_LOGGING_CONFIG = dict(
    version=1,
    disable_existing_loggers=True,
    formatters=DEFAULT_LOG_FORMATTER,
    handlers=DEFAULT_LOG_CONSOLE_HANLDER,
    root=DEFAULT_ROOT_LOGGER,
)
