import export

export.init(default=export.PUBLIC)


def foo():
    pass


@export.private
def bar():
    pass


@export.private
def baz():
    pass
