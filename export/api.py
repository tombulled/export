import inspect
import sys
from types import ModuleType
from typing import List, Mapping, Optional, Sequence, Set, TypeVar

from .enums import Access
from .models import Scope
from .protocols import Named

__all__: Sequence[str] = ("init", "public", "private")


T = TypeVar("T", bound=Named)


def init(*, default: Access = Access.PRIVATE) -> None:
    module: Optional[ModuleType] = inspect.getmodule(inspect.stack()[1][0])

    class Module(ModuleType):
        _scope: Scope = Scope(default=default)

        @property
        def __all__(self) -> List[str]:
            attributes: Set[str] = {key for key in dir(self) if not key.startswith("_")}

            if self._scope.default is Access.PUBLIC:
                return sorted(attributes - self._scope.private)

            return sorted(self._scope.public)

    module.__class__ = Module


def public(obj: T, /) -> T:
    return _export(obj, access=Access.PUBLIC)


def private(obj: T, /) -> T:
    return _export(obj, access=Access.PRIVATE)


def _export(obj: T, /, access: Access) -> T:
    module: ModuleType = sys.modules[obj.__module__]

    collections: Mapping[Access, Set[str]] = {
        Access.PUBLIC: module._scope.public,
        Access.PRIVATE: module._scope.private,
    }

    collection: Set[str] = collections[access]

    collection.add(obj.__name__)

    return obj
