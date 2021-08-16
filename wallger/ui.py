"""
Here I define everything related to Colorama
"""

from colorama import Style, Fore

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


def cprint(txt: str, color: str = red, brightness: str = normal, **kwargs) -> None:
    """
    Print the text with colors.
    """
    print(f"{brightness}{color}{txt}{reset}", **kwargs)
