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
>>> # 'foo' was exported
>>> lib.foo()
'foo'
>>>
>>> # 'bar' was not exported
>>> lib.bar()
NameError: name 'bar' is not defined
```
