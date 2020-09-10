from datetime import datetime
from time import sleep

# DESCRIPTOR SHOULD GET AND SET VALUE TO INSTANCE, OTHERWISE value will be shared

class TimeUTC:
    def __get__(self, instance, owner):
        # print(f"__get__ called, self={self}, instance={instance}, owner_class={owner}\n{datetime.utcnow().isoformat()}")
        if instance is None:
            return self
        else:
            return datetime.utcnow().isoformat()


class Logger1:
    current_time = TimeUTC()

class Logger2:
    current_time = TimeUTC()

# print(Logger1.current_time)
# print(Logger2.current_time)

l1 = Logger1()
l2 = Logger2()

# sleep(5)
# print(l1.current_time)
# print(l2.current_time)

# -------------------------------------------------------------------

class OneDigitNumericValue():
    def __init__(self):
        print("__init__ called")

    def __set_name__(self, owner, name):
        self.name = name
        print("__set_name__ called")
        print("self.name:", self.name)
        # print("self:", self)
        # print("owner1:", owner)


    def __get__(self, obj, owner=None) -> object:
        # print("obj:", obj)
        # print("owner:", owner)
        if obj is None:
            return self
        print(f"__get__ called")
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

class Foo():
    number = OneDigitNumericValue()

# __set_name__ is called once when class object is created, not when instance is created
# try, it will print line 40 without an explicit print statement

# __get__ and __set__ are called when dot notation is invoked from the instance


# for data descriptor (get and set implemented) dot notation will call get/set first and go to dictionary afterwards
# for non-data descriptor (only get) dot notation will look for the instance attr in the instance dict first,


f1 = Foo()
# f1.number = 2
# print(f1.__dict__)
f1.__dict__["number"] = 3
# print(f1.__dict__)
print(f1.number)


# print(my_foo_object.__dict__)
# print(Foo.__dict__)


# print(my_foo_object.number)
#
#
# print(my_second_foo_object.number)
# print(my_second_foo_object.__dict__)
#
# my_third_foo_object = Foo()
# print(my_third_foo_object.number)
# print(my_third_foo_object.__dict__)


# data descriptor, defaults to __get__ method first
class IntegerValue:
    def __set__(self, instance, value):
        print(f'__set__ called... on {instance} with value: {value}')

    def __get__(self, instance, owner_class):
        print(f'__get__ called... on {instance} {owner_class}')

class Point:
    x = IntegerValue()

p = Point()

# p.x = 100
# print(p.x) #None
# print(p.__dict__) #None
# p.__dict__["x"] = 100
# print(p.__dict__)
# print(p.x) # None


# non-data descriptor, defaults to __dict__ first (__get__ not called because there is already x in the dictionary)
class IntegerValue:
    def __get__(self, instance, owner_class):
        print(f'__get__ called... on {instance} {owner_class}')

class Point:
    x = IntegerValue()

p = Point()

p.x = 100
# print(p.x) #100
# print(p.__dict__) #{'x': 100}
# print(p.x) # 100


#  ============== PROPERTIES AND DESCRIPTORS ======================
from numbers import Integral

class Person:

    def get_age(self):
        return getattr(self, "_age", None)


    def set_age(self, value):
        if not isinstance(value, Integral):
            raise ValueError("age must be an integer")
        if value < 0 :
            raise ValueError("age must be a non negativ einteger")
        self._age = value


    age = property(fget=get_age, fset=set_age)

p = Person()

try:
    p.age = -10
except ValueError as ex:
    print(ex)

print(p.__dict__) #empty
print(Person.age) #<property object at 0x000001B9ED6FADB8>
print(hasattr(Person.age, "__get__"), hasattr(Person.age, "__set__")) #true true
#property is a data descriptor obj, hence it has __get__ and __set__ method implemented
