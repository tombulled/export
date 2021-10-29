import sys
import types
import typing

def export(obj):
    module: types.ModuleType = sys.modules[obj.__module__]

    if not hasattr(module, '__all__'):
        module.__all__: typing.List[str] = []

    module.__all__.append(obj.__name__)

    return obj
