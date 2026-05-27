import logging

from utils_base.console.constants.COLOR_FOREGROUND import COLOR_FOREGROUND
from utils_base.console.constants.COLOR_FORMAT import COLOR_FORMAT

LEVEL_TO_STYLE = {
    logging.CRITICAL: dict(
        foreground=COLOR_FOREGROUND.WHITE,
        format=COLOR_FORMAT.BOLD,
    ),
    logging.ERROR: dict(
        foreground=COLOR_FOREGROUND.RED,
    ),
    logging.WARNING: dict(
        foreground=COLOR_FOREGROUND.YELLOW,
    ),
    logging.INFO: dict(
        foreground=COLOR_FOREGROUND.GREEN,
    ),
    logging.DEBUG: dict(
        foreground=COLOR_FOREGROUND.WHITE,
        format=COLOR_FORMAT.FAINT,
    ),
    logging.NOTSET: dict(
        foreground=COLOR_FOREGROUND.WHITE,
    ),
}
