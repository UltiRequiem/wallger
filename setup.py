from setuptools import setup


setup(
    name="wallger",
    packages=["wallger"],
    version="0.4.0",
    license="MIT",
    description="Wallpaper changer for Linux, get images from Wallhaven, Unsplash and others!",
    author="Eliaz Bobadilla",
    url="https://github.com/UltiRequiem/wallger",
    keywords=["unsplash", "wallhaven", "feh", "wallpaper", "cli"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["wallger = wallger.wallger:main"]},
    install_requires=["requests==2.25.1"],
)
