import dataclasses
import typing

from . import enums

@dataclasses.dataclass
class Scope:
    default: enums.Visibility = enums.Visibility.PRIVATE
    exports: typing.Dict[enums.Visibility, typing.Set[str]] = dataclasses.field(
        default_factory=lambda: {
            visibility: set()
            for visibility in enums.Visibility
        }
    )