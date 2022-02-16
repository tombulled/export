import visibility

visibility.init(default=visibility.PRIVATE)

@visibility.public
def foo():
    pass

def bar():
    pass

def baz():
    pass