import logging

from rich.console import Console
from rich.logging import RichHandler

console = Console()
_RHandler = RichHandler(console=console, rich_tracebacks=True)


logging.getLogger("trakteer").setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M"
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(_RHandler)
_RHandler.setFormatter(formatter)
