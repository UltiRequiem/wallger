"""
Core of the Project
"""

from .helpers import get_config_file
from .ui import cprint


def main() -> None:
    """
    Initialize the Process
    """
    config = get_config_file()
    cprint(config)
