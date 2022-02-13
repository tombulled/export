import enum
import types
import sys

class Visibility(enum.Enum):
    PUBLIC = enum.auto()
    PRIVATE = enum.auto()

PUBLIC = Visibility.PUBLIC
PRIVATE = Visibility.PRIVATE

# def init(default: Visibility = Visibility.PRIVATE) -> None:
#     return ['foo']

def public(func):
    _export(func)

# def private(func):
#     _export(func)

def _export(func):
    module: types.ModuleType = sys.modules[func.__module__]

    if not hasattr(module, '__all__'):
        module.__all__ = []

    module.__all__.append(func.__name__)

    return func