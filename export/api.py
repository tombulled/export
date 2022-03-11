import inspect
import sys
import types
import typing

from . import enums, models


def init(*, default: enums.Access = enums.Access.PRIVATE) -> None:
    module: types.ModuleType = inspect.getmodule(inspect.stack()[1][0])

    class Module(types.ModuleType):
        _scope: models.Scope = models.Scope(default=default)

        @property
        def __all__(self) -> typing.List[str]:
            attributes: typing.Set[str] = {
                key for key in dir(self) if not key.startswith("_")
            }

            if self._scope.default == enums.Access.PUBLIC:
                return sorted(attributes - self._scope.private)

            return sorted(self._scope.public)

    module.__class__ = Module


def public(obj: typing.T) -> typing.T:
    return _export(obj, access=enums.Access.PUBLIC)


def private(obj: typing.T) -> typing.T:
    return _export(obj, access=enums.Access.PRIVATE)


def _export(obj: typing.T, access: enums.Access) -> typing.T:
    module: types.ModuleType = sys.modules[obj.__module__]

    collection: typing.Set[str] = (
        module._scope.public if access is enums.Access.PUBLIC else module._scope.private
    )

    collection.add(obj.__name__)

    return obj
