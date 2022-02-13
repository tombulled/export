import visibility

__all__ = visibility.init(default=visibility.PUBLIC)

def foo():
    pass

@visibility.private
def bar():
    pass