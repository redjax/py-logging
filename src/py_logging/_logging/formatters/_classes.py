from __future__ import annotations

import logging
from logging import handlers

class Logger(object):
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "crit": logging.CRITICAL,
    }  # relationship mapping

    def __init__(
        self,
        filename,
        level="info",
        rotate_when="D",
        backup_count=3,
        fmt="%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s",
    ):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # Setting the log format
        self.logger.setLevel(self.level_relations.get(level))  # Setting the log level
        console_handler = logging.StreamHandler()  # on-screen output
        console_handler.setFormatter(format_str)  # Setting the format
        th = handlers.TimedRotatingFileHandler(
            filename=filename,
            when=rotate_when,
            backupCount=backup_count,
            encoding="utf-8",
        )  # automatically generates the file at specified intervals
        th.setFormatter(format_str)  # Setting the format
        self.logger.addHandler(console_handler)  # Add the object to the logger
        self.logger.addHandler(th)
