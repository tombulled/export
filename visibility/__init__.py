import enum
import types
import sys
import inspect
import typing
import pprint

# TODO: Make this a NoValue enum
class Visibility(enum.Enum):
    PUBLIC = enum.auto()
    PRIVATE = enum.auto()

PUBLIC = Visibility.PUBLIC
PRIVATE = Visibility.PRIVATE

def init(default: Visibility = Visibility.PRIVATE) -> None:
    module = inspect.getmodule(inspect.stack()[1][0])

    class Module(types.ModuleType):
        _default = default
        _public = {}
        _private = {}

        @property
        def __all__(self):
            attributes = [attr for attr in dir(self) if not attr.startswith('_')]

            pprint.pprint({
                'default': self._default,
                'public': self._public,
                'private': self._private,
                'attrs': attributes,
            })

            if default is Visibility.PUBLIC:
                return list((set(attributes) | set(self._public)) - set(self._private))

            return list(set(self._public) - set(self._private))

    # NOTE: What if hasattr(module, '__all__')?

    module.__class__ = Module

def public(func):
    # Note: What if two functions with the same name exist, only one of which is exported?

    module = sys.modules[func.__module__]

    module._public[func.__name__] = func

def private(func):
    module = sys.modules[func.__module__]

    module._private[func.__name__] = func