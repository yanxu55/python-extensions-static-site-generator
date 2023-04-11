import sys, importlib
from pathlib import Path


def load_module(directory, name):
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)


def load_directory(directory):
    for path in Path(directory).rglob("*.py"):
        module = path.stem
        load_module(str(path.parent), module)


def load_bundled():
    directory = Path(__file__).parent / "bundled"   
    load_directory(directory)

    