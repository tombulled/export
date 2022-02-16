import visibility

visibility.init(default=visibility.PUBLIC)

def foo():
    pass

@visibility.private
def bar():
    pass

@visibility.private
def baz():
    pass