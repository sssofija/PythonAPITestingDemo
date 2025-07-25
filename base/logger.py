import logging
import sys
import colorlog


def get_logger() -> logging.Logger:
    root = logging.getLogger()
    if not root.handlers:
        root.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(
            colorlog.ColoredFormatter(
                "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - %(lineno)d"
            )
        )
        root.addHandler(handler)

    return root


logger = get_logger()

