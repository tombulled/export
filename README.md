# export
Expose module functionality

## Usage
```python
# lib.py

import export

@export
def foo(): pass

def bar(): pass

@export
class Foo: pass

class Bar: pass
```

```python
>>> from lib import *
>>>
>>> foo
<function foo at 0x7f429bfe3040>
>>> Foo
<class 'lib.Foo'>
>>>
>>> bar
NameError: name 'bar' is not defined
>>> Bar
NameError: name 'Bar' is not defined
>>>
```
