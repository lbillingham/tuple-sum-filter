import logging
import sys
from os import environ

import structlog

PROD_PROCESSORS = [
    structlog.stdlib.filter_by_level,
    structlog.processors.TimeStamper(),
    structlog.processors.StackInfoRenderer(),
    structlog.processors.format_exc_info,
    structlog.processors.JSONRenderer(),
]

DEV_PROCESSORS = [structlog.dev.set_exc_info, structlog.dev.ConsoleRenderer()]

PROCESSORS = (
    [*PROD_PROCESSORS, *DEV_PROCESSORS]
    if environ.get("ENVIRONMENT") == "DEV"
    else PROD_PROCESSORS
)

logging.basicConfig(stream=sys.stdout, format="%(message)s")

structlog.configure(
    processors=PROCESSORS,  # type: ignore  ## mypy is confused by processor unpacking
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

get_logger = structlog.get_logger
