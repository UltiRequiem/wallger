"""
This file tells Python that this is a submodule
"""

from .core import main

# Package Data
__version__ = "0.7.3"
__description__ = (
    "Wallpaper changer for Linux, get images from Wallhaven, Unsplash and others!",
)

# So Pyrigth does not mark main as not used
if __name__ == "__main__":
    main()
