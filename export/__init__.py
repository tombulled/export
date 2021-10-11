import sys
import types
import typing

class ExportModule(types.ModuleType):
    @staticmethod
    def export(obj):
        module: types.ModuleType = sys.modules[obj.__module__]

        if not hasattr(module, '__all__'):
            module.__all__: typing.List[str] = []

        # TODO: Remove duplicates
        module.__all__.append(obj.__name__)

        return obj

    __call__ = export

sys.modules[__name__].__class__ = ExportModule
