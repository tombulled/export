# export
Export data

## Usage
```python
# lib.py

import export

@export
def foo():
    return 'foo'

def bar():
    return 'bar'
```

```python
>>> from lib import *
>>>
>>> lib.foo()
'foo'
>>> lib.bar()
NameError: name 'bar' is not defined
```
