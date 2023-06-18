from dataclasses import dataclass, field
from typing import Sequence, Set

from .enums import Access

__all__: Sequence[str] = ("Scope",)


@dataclass
class Scope:
    default: Access = Access.PRIVATE
    public: Set[str] = field(default_factory=set)
    private: Set[str] = field(default_factory=set)
