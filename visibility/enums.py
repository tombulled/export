import enum

class NoValue(enum.Enum):
    def __repr__(self) -> str:
        return f'<{type(self).__name__}.{self.name}>'

class Visibility(NoValue):
    PUBLIC = True
    PRIVATE = False

    def inverse(self):
        return type(self)(not self.value)