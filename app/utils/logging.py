"""
Project Chimera: Logging setup and configuration.
"""
import logging
import sys
from typing import Optional


def setup_logging(
    level: str = "INFO",
    format_string: Optional[str] = None,
    stream: Optional[sys.__class__] = None,
) -> None:
    """
    Configure application logging.

    :param level: Log level (DEBUG, INFO, WARNING, ERROR)
    :param format_string: Optional custom format
    :param stream: Optional stream (default stderr)
    """
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format=format_string,
        stream=stream or sys.stderr,
    )
