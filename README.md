# visibility

## Usage
### Allowlist
```python
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
```

### Denylist
```python
import visibility

visibility.init(default=visibility.PRIVATE)

@visibility.public
def foo():
    pass

def bar():
    pass

def baz():
    pass
```