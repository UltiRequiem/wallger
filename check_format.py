from os import system

files = [
    "wallger/__init__.py",
    "wallger/__main__.py",
    "wallger/helpers.py",
    "wallger/run.py",
    "wallger/version.py",
    "wallger/providers/__init__.py",
    "wallger/providers/local.py",
    "wallger/providers/provider.py",
    "wallger/providers/unsplash.py",
    "wallger/providers/wallhaven.py",
]


def check_format():
    for i in files:
        system(f"pycodestyle --show-source --show-pep8 --format=default {i}")


if __name__ == "__main__":
    check_format()
    print("All done!")
