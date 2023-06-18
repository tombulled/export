from enum import Enum, auto
from typing import Sequence

__all__: Sequence[str] = ("Access",)


class Access(Enum):
    PUBLIC = auto()
    PRIVATE = auto()

    def __repr__(self) -> str:
        return f"<{type(self).__name__}.{self.name}>"
