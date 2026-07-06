import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger() -> logging.Logger:
    """
    Configure and return the application logger.
    """

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / "monitor.log"

    handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=1024 * 1024,   # 1 MB
        backupCount=5
    )

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    return logging.getLogger("linux-health-monitor")