from loguru import logger
import sys

logger.remove()

logger.add(
    "smart_awake.log",
    rotation="1 MB",
    retention="5 days",
    level="INFO"
)

if sys.stdout is not None:
    logger.add(sys.stdout, level="INFO")