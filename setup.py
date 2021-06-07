from setuptools import setup
from wallger.version import __version__


setup(
    name="wallger",
    packages=["wallger"],
    version=__version__,
    license="MIT",
    description="Wallpaper changer for Linux, get images from Wallhaven, Unsplash and others!",
    author="Eliaz Bobadilla",
    url="https://github.com/UltiRequiem/wallger",
    keywords=["unsplash", "wallhaven", "feh", "wallpaper", "cli"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["wallger = wallger.run:main"]},
    install_requires=["requests==2.25.1"],
)
