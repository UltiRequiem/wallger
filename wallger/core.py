"""
Core of the Project
"""

from .helpers import get_config_file, select_provider


def main() -> None:
    """
    Initialize the Process
    """
    select_provider(get_config_file())
