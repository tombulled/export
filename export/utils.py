import sys
import types

def make_callable(module: str, func: callable) -> None:
    class CallableModule(types.ModuleType):
        __call__ = staticmethod(func)

    sys.modules[module].__class__: type = CallableModule
