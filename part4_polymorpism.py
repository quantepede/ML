
# polymorphism is the ability to define a generic functionality that will potentially behave differently
# when applied to different types
# ie addition operator works with strings and numbers, duck typing, obj that support iterable protocol (list, tuple, dict)

# hashing and equality
from collections import defaultdict


class Person():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __len__(self):
        print(f"len called")
        return len(self.name)

    def __bool__(self):
        print("bool called")
        return len(self) > 0

p1 = Person("Eric")
d = {p1: "Eric"}
p2 = Person("Eric")

# print(p1 == p2)
# print(p1.__hash__(), p2.__hash__())

# ========================== booleans
# __bool__ returns True if len>0, otherwise False
# The way Python determines the truth value of our custom classes is to:
#
# first look for an implementation of the __bool__ method (which needs to return a boolean)
# if not present, looks for __len__ and will return False if that is 0, and True otherwise
# otherwise returns True


print(bool(p1))
print(len(p1))

p3 = Person("")

print(bool(p3))
print(len(p3))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        return bool(self.x or self.y)

p1 = Point(0, 0)
p2 = Point(1, 1)

print(bool(p1), bool(p2))

# ========================================== callables
# We can make instances of our classes callables by implementing the __call__ method.
from functools import partial

class Person():
    def __call__(self, *args, **kwargs):
        print(f"__call__ called")

    pass

new = Person()
new()
print(callable(new))
print(type(new), type(Person))
print(type(partial))

# use pythons partial from functools

def func(a,b,c):
    return a,b,c

new_partial_func = partial(func, 10, 20)

print(new_partial_func(30))

# create partial class from scratch to mimic same behaviour

class PartialCustom:
    def __init__(self, func, *args):
        self._func = func
        self._args = args

    def __call__(self, *args):
        return self._func(*self._args, *args)

new_partial_func = PartialCustom(func, 10, 20)

print(new_partial_func(40))

# every class in python is callable because we can create an instance off of it
print([callable(x) for x in (object, type, PartialCustom)])



# =================== default dict and using callable as default value

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

for k, v in s:
    d[k].append(v)
    # print(d.items())

print(d["a"])
print(d.items())
print(d["yellow"])

# When each key is encountered for the first time, it is not already in the mapping; so an entry is
# automatically created using the default_factory function which returns an empty list. The list.append()
# operation then attaches the value to the new list. When keys are encountered again, the look-up proceeds
# normally (returning the list for that key) and the list.append() operation adds another value to the list.


# similarly When a letter is first encountered, it is missing from the mapping, so the default_factory
# function calls int() to supply a default count of zero. The increment operation then builds up the count
# for each letter.

# s = 'mississippi'
# d = defaultdict(int)
# for k in s:
#     d[k] += 1
# d.items()
# # [('i', 4), ('p', 2), ('s', 4), ('m', 1)]


# we can create a callable and pass to default dict to create a custom default value

class DefaultValue:
    def __init__(self, default):
        self.counter = 0
        self.default = default

    def __call__(self):
        self.counter += 1
        return self.default




newdefault = DefaultValue("N/A")
newdict = defaultdict(newdefault)


print(newdict["a"])
print(newdict.items())

# ========== writing a decorator class and using __call__ to calculate avg time and number of times a function is called

import time
import random

class Timer:

    def __init__(self, fn):
        self.fn = fn
        self.counter = 0
        self.total_elapsed = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        begin = time.time()
        result = self.fn(*args, **kwargs)
        time.sleep(random.random())

        end = time.time()

        self.total_elapsed += (end - begin)

        return result

    @property
    def avg_time(self):
        return self.total_elapsed / self.counter


@Timer
def func1(a,b):
    return a,b

print(func1(1,2), func1(122,12), func1.counter, func1.total_elapsed, func1.avg_time)

# ========== del method ======================
# it is rare for devs to use the __del__ method for critical things like closing a file, or closing committing a transaction in a database, etc - instead use a context manager, and avoid using the __del__ method.
#
# Because you do not know when the __del__ method is going to get called (unless you know exactly how your
# code might be creating references to the object), you could also get into a situation where other objects
# (like global objects) referenced in the __del__ method will even still be around by the time __del__
# is called (it would get called when the module is destroyed, such as at program shutdown).
