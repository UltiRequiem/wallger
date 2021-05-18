import importlib

def dynamic_import(module):
    try:
        return importlib.import_module(module)
    except ImportError as e:
        print(f"Oops {e} ocurred.")
