from importlib import import_module


def dynamic_import(module):
    try:
        return import_module(module)
    except ImportError as e:
        print(f"Oops {e} ocurred.")
