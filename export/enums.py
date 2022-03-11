import enum


class Access(enum.Enum):
    PUBLIC = enum.auto()
    PRIVATE = enum.auto()

    def __repr__(self) -> str:
        return f"<{type(self).__name__}.{self.name}>"
