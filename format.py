from os import system

files = [
    "wallger/__init__.py",
    "wallger/__main__.py",
    "wallger/helpers.py",
    "wallger/run.py",
    "wallger/version.py",
    "wallger/providers/__init__.py",
    "wallger/providers/local.py",
    "wallger/providers/unsplash.py",
    "wallger/providers/wallhaven.py",
]


def format():
    for i in files:
        system(f"autopep8 --in-place --aggressive {i}")


if __name__ == "__main__":
    format()
    print("All done!")
