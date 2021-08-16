"""
Colorama Configuration
"""

from colorama import Fore, Style

# For export, and easily usage :)
red, green, yellow, blue, magenta, cyan, normal, reset = (
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Style.NORMAL,
    Style.RESET_ALL,
)


def cprint(txt, color: str = blue, brightness: str = normal, **kwargs) -> None:
    """
    Print the text with colors.
    """
    print(f" {brightness}{color}{txt}{reset}", **kwargs)


def error_print(txt: str, brightness: str = normal, **kwargs) -> None:
    """
    Print the error.
    """
    cprint(txt, red, brightness, **kwargs)
