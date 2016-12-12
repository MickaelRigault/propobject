# propobject
Source Object to inherit from to help building clean classes

[![PyPI](https://img.shields.io/pypi/v/propobject.svg?style=flat-square)](https://pypi.python.org/pypi/propobject)

## How to use propobject

This module enables to easily make use of @property decorator to create simple (to read and to use) object oriented python.
propobject is built upon 3 object global variables:
- PROPERTIES
- SIDE_PROPERTIES
- DERIVED_PROPERTIES

While you build an new object, you should define in one of the above entries the name of the variable you have. You can set it to any of them but you are invited to use PROPERTIES for the fundamental entries, SIDE_PROPERTIES for the optional entries and DERIVED_PROPERTIES for the variable created by the class, i.e. that can not be set by the user.

When you generate an instance of your object, the entries `_properties`, `_side_properties` and `_derived_properties` will be created. These are dictionaries containing the entries for the PROPERTIES, SIDE_PROPERTIES and DERIVED_PROPERTIES. By default, they are None.

For instance:
```
from propobject import BaseObject

class Foo( BaseObject):
    PROPERTIES = ["a","b"]
    SIDE_PROPERTIES = ["aa","bb"]
    DERIVED_PROPERTIES = ["derived_v"]
    
    @property
    def a(self):
        return self._properties['a']
    
    
```

Inherating an object conserves the PROPERTIES, SIDE_PROPERTIES, DERIVED_PROPERTIES

```
class FooFoo( Foo ):
    PROPERTIES = ["c"]
    
    @property
    def a2(self):
        return self._properties['a']**2

    @property
    def c(self):
        return self._properties['c']**2
     
```



