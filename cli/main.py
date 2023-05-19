
from rich.console import Console
from rich.logging import RichHandler
import logging
import typer

console = Console()

# Setup the Rich logger
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console)],
)

logger = logging.getLogger("rich")

app = typer.Typer(name="juggernaut")


