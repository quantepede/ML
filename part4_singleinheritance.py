class Shape:
    pass

class Polygon(Shape):
    pass

class Square(Polygon):
    pass

sq = Square()

# issubclass and isinstance follow hierarchy to higher levels
print("-")
print(issubclass(Square, Shape))
print(issubclass(Square, Polygon))

print(isinstance(sq, Shape))
print(isinstance(sq, Polygon))

# all classes are instances of type/object class and all classes have type (type)
print("-")
print(isinstance(Square, type))
print(isinstance(Square, object))

# all classes are sublasses of object (not type)
print("-")
print(issubclass(Square, object))
print(issubclass(Square, type))

# type shows which class the instance is directly created from (not parents)
print("-")
print(type(sq), type(Square))

# object and type are instances of each other (circular reference, can not be expressed in Python)
print("-")
print(isinstance(type, object))
print(isinstance(object, type))

# type is a subclass of object, but object is not a subclass of type
print(issubclass(type, object))
print(issubclass(object, type))

# since every object iin Python (classes, functions, modules etc inherits from object, they come
# with certain functionality implemented already (init, eq, repr, str etc)

o1 = object()
print(dir(object))
print(o1)

# also type of all built-in Python objects (int, float, class etc) will be type
class Sample:
    pass
print(type(Sample))
print(type(int))

# other types live in the types module (function type, generator type etc)
import types

print(dir(types))

def fun():
    pass

print(types.FunctionType is type(fun))
print(isinstance(fun, types.FunctionType))

#  ====================== OVERRIDING ==================
# why super() does not support setter methods
# Python super and setting parent class property
# https://stackoverflow.com/questions/10810369/python-super-and-setting-parent-class-property
# https://bugs.python.org/issue14965


class Try:
    def __init__(self, value):
        self._attribute = value

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value

instance1 = Try(10)

print(instance1.__dict__)
print(instance1.attribute)
