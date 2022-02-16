# visibility
Control module exports

## About
This library dynamically generates an `__all__` attribute for modules

## Usage

### Allowlist Approach
*Doesn't* export objects marked **private**, *does* export everything else

```python
# lib.py

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

```python
>>> import lib
>>> 
>>> lib.__all__
['foo', 'visibility']
```

### Denylist Approach
*Does* export objects marked **public**, *doesn't* export everything else

```python
# lib.py

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

```python
>>> import lib
>>> 
>>> lib.__all__
['foo']
```