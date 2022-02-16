import enum

class NoValue(enum.Enum):
    def __repr__(self) -> str:
        return f'<{type(self).__name__}.{self.name}>'

class Visibility(NoValue):
    PUBLIC = enum.auto()
    PRIVATE = enum.auto()