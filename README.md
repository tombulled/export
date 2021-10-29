# export
Selectively expose module functionality

## Usage
**lib.py**
```python
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
>>> # Exported functionality is added to the library's `__all__`
>>> lib.__all__
['foo']
>>>
>>> # 'foo' was exported
>>> lib.foo()
'foo'
>>>
>>> # 'bar' was not exported
>>> lib.bar()
NameError: name 'bar' is not defined
```
