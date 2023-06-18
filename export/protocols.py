from typing import Protocol, Sequence

__all__: Sequence[str] = ("Named",)


class Named(Protocol):
    __name__: str
