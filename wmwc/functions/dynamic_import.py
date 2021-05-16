import importlib

def dynamic_import(module):
    module =f"wmwc.providers.{module}"
    return importlib.import_module(module)
