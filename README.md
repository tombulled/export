# export
Control module exports

## About
This library dynamically generates an `__all__` attribute for modules

## Install
```console
pip install export
```

## Usage

### Private by Default
*Does* export objects marked **public**, *doesn't* export everything else

```python
# lib.py

import export

export.init(default=export.PRIVATE)

@export.public
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

### Public by Default
*Doesn't* export objects marked **private**, *does* export everything else

```python
# lib.py

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
```

```python
>>> import lib
>>> 
>>> lib.__all__
['export', 'foo']
```
