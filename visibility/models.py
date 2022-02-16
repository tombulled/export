import dataclasses
import typing

from . import enums

@dataclasses.dataclass
class Scope:
    default: enums.Visibility = enums.Visibility.PRIVATE
    public: typing.Set[str] = dataclasses.field(default_factory=set)
    private: typing.Set[str] = dataclasses.field(default_factory=set)