import logging
import sys
from logging.handlers import TimedRotatingFileHandler

# FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "my_app.log"


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)  # The repr() function returns a printable representation of the given object

    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result


def get_console_handler(formatter):
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    return console_handler


def get_file_handler(formatter):
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(formatter)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # better to have too much log than not enough in dev/staging
    one_line_formatter = OneLineExceptionFormatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    logger.addHandler(get_console_handler(one_line_formatter))
    logger.addHandler(get_file_handler(one_line_formatter))
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger
