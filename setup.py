from setuptools import setup
from wallger import __version__, __author__


setup(
    name="wallger",
    packages=["wallger", "wallger.core", "wallger.providers"],
    version=__version__,
    license="MIT",
    description="Wallpaper changer for Linux, get images from Wallhaven, Unsplash and others!",
    author=__author__,
    url="https://github.com/UltiRequiem/wallger",
    keywords=["unsplash", "wallhaven", "feh", "wallpaper", "cli"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
