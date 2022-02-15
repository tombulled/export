import visibility

visibility.init(default=visibility.PUBLIC)

@visibility.public
def foo():
    pass

@visibility.private
def bar():
    pass

def baz():
    pass