import inspect
import sys
import types
import typing

from . import enums, models

def init(*, default: enums.Visibility = enums.Visibility.PRIVATE) -> None:
    module: types.ModuleType = inspect.getmodule(inspect.stack()[1][0])

    class Module(types.ModuleType):
        _scope: models.Scope = models.Scope(
            default = default,
        )

        @property
        def __all__(self) -> typing.List[str]:
            attributes: typing.Set[str] = {
                key
                for key in dir(self)
                if not key.startswith('_')
            }

            return sorted(attributes - self._exports[self._default.inverse()])

    module.__class__ = Module

def public(obj: typing.T) -> typing.T:
    module: types.ModuleType = sys.modules[obj.__module__]

    module._scope.exports[enums.Visibility.PUBLIC].add(obj.__name__)

    return obj

def private(obj: typing.T) -> typing.T:
    module: types.ModuleType = sys.modules[obj.__module__]

    module._scope.exports[enums.Visibility.PRIVATE].add(obj.__name__)

    return obj