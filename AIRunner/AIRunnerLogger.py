from typing import Any, Optional
import logging

DEFAULT = " %(asctime)s %(message)s (%(filename)s:%(lineno)d)"


class ColorizedFormatter(logging.Formatter):
    fmt: str

    def format(self, record: logging.LogRecord) -> str:
        white_fg = "\x1b[37;20m"
        black_fg = "\x1b[30;20m"
        red_fg = "\x1b[31;20m"

        yellow_bg = "\x1b[43;20m"
        red_bg = "\x1b[41;20m"
        gray_bg = "\x1b[100;20m"
        bold = "\x1b[1m"
        reset = "\x1b[0m"

        header = "%(name)-8s -> %(levelname)+8s "

        if record.levelno == logging.DEBUG:
            formatter = logging.Formatter(
                f"{bold}{black_fg}{header}{reset} {DEFAULT}", "%H:%M:%S"
            )
            return formatter.format(record)
        elif record.levelno == logging.INFO:
            formatter = logging.Formatter(
                f"{gray_bg}{header}{reset} {DEFAULT}", "%H:%M:%S"
            )
            return formatter.format(record)
        elif record.levelno == logging.WARNING:
            formatter = logging.Formatter(
                f"{yellow_bg}{black_fg}{header}{reset} {DEFAULT}", "%H:%M:%S"
            )
            return formatter.format(record)
        elif record.levelno == logging.ERROR:
            formatter = logging.Formatter(
                f"{red_bg}{white_fg}{header}{reset} {DEFAULT}", "%H:%M:%S"
            )
            return formatter.format(record)
        elif record.levelno == logging.CRITICAL:
            formatter = logging.Formatter(
                f"{red_bg}{white_fg}{header}{reset} {red_fg}{bold}{DEFAULT}{reset}",
                "%H:%M:%S",
            )
            return formatter.format(record)
        else:
            return ""


class DefaultFormatter(logging.Formatter):
    fmt: str

    def format(self, record: logging.LogRecord) -> str:
        header = "%(name)s -> %(levelname)s"

        if record.levelno == logging.DEBUG:
            formatter = logging.Formatter(f"{header} {DEFAULT}", "%H:%M:%S")
            return formatter.format(record)
        elif record.levelno == logging.INFO:
            formatter = logging.Formatter(f"{header} {DEFAULT}", "%H:%M:%S")
            return formatter.format(record)
        elif record.levelno == logging.WARNING:
            formatter = logging.Formatter(f"{header} {DEFAULT}", "%H:%M:%S")
            return formatter.format(record)
        elif record.levelno == logging.ERROR:
            formatter = logging.Formatter(f"{header} {DEFAULT}", "%H:%M:%S")
            return formatter.format(record)
        elif record.levelno == logging.CRITICAL:
            formatter = logging.Formatter(f"{header} {DEFAULT}", "%H:%M:%S")
            return formatter.format(record)
        else:
            return ""


class AIRunnerLogger:
    def __init__(
        self, name: str, colorize: Optional[bool] = None, level: Optional[str] = "DEBUG"
    ) -> None:
        self.name = name
        self.colorize = colorize if colorize is not None else False
        self.level = level

        # create logger with 'spam_application'
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level or "DEBUG")

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        if self.colorize:
            ch.setFormatter(ColorizedFormatter())
        else:
            ch.setFormatter(DefaultFormatter())

        self.logger.addHandler(ch)

    def info(self, message: str, *args: Any, **kwargs: Any) -> None:
        self.logger.info(message, *args, **kwargs)

    def debug(self, message: str, *args: Any, **kwargs: Any) -> None:
        self.logger.debug(message, *args, **kwargs)

    def warning(self, message: str, *args: Any, **kwargs: Any) -> None:
        self.logger.warning(message, *args, **kwargs)

    def error(self, message: str, *args: Any, **kwargs: Any) -> None:
        self.logger.error(message, *args, **kwargs)

    def critical(self, message: str, *args: Any, **kwargs: Any) -> None:
        self.logger.critical(message, *args, **kwargs)
