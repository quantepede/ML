class MyClass():
    # class attributes (not attributes of the instance)
    language = "Python"
    version = "3.6"

    def say_hello(self):
        print("hello world")
    pass

# print(type(type))
# print(MyClass.__name__)
#
# new = MyClass()
# print(type(new))
#
# print(new.__class__)
#
# help(type)
#
# print(getattr(MyClass, "language"))
#
# setattr(MyClass, "version", "3.7")
#
# print(MyClass.version)
#
# setattr(MyClass, "x", "dynamically added attribute")
#
# print(MyClass.x)
#
# # state of the class is stored in a dict (dunder method)
# print(MyClass.__dict__)
# print(MyClass.__dict__["language"])
#
# delattr(MyClass, "x")
# print(MyClass.__dict__)
# # print(MyClass.__dict__["x"])
#
# # an attribute can also be a callable
# print(MyClass.__dict__)
#
# # classes are also callable
# a = MyClass.__call__()
# b = MyClass()
# # print(a)
# # print(b)
#
# # instances have their own namespace
# print(a.__dict__)
# print(a.language)
# print(type(a))

# # overriding __class__ (related to metaprogramming)
# # type isnt fooled so used that. also isinstance recognizes both
# class NewClass():
#     __class__ = str
#
# new = NewClass()
# print(type(new))
# print(new.__class__)
# print(isinstance(new,NewClass))
# print(isinstance(new,str))

# when python cannot find an attribute in instance dict, looks for it in the class dict
# if class dict changes, all instances inherit
# if instance dict changes, only that obj is affected

# class Bank():
#     rate = 1.2
#
# bank1 = Bank()
# bank2 = Bank()
#
# print(bank1.__dict__)
# bank1.savingrate = 1.5
# print(bank1.savingrate)
#
# Bank.rate = 1.6
#
# print(bank1.savingrate, bank1.rate, bank2.rate)



# # function attributes
# class Printer():
#
#     # if self (or sth else) is not given, cant call this from an instance
#     def say_hello(self):
#         print("hello")
#
#
# a = Printer()
# print(Printer.say_hello)
# print(a.say_hello)
#
# # say_hello function is bound to the class instance, so when it`s called,
# # instance obj is passed as the first parameter
#
# # same
# print(a.say_hello())
# print(Printer.say_hello(a))
#
# # bound method say_hello has access to a`s namespace, and has dunder method __self__ that returns it
# print(a.say_hello.__self__)
# # similarly, bound method say_hello has dunder method __func__ which returns the original function
# print(a.say_hello.__func__)
#
# # method (unlike function) needs to be bound to sth
# print(type(Printer.say_hello))
# print(type(a.say_hello))

# class Person():
#     def say_hello(self):
#         print(f"{self} says hello")
#
#
# p = Person()
#
# print(hex(id(p)))
# print(p.say_hello)
# print(Person.say_hello)
# print(p.__dict__)
#
#
# # monkey patching: adding functions to or modifying other attributes of to class in runtime
# # instances inherit changes made to class object and those functions (if they have self) become
# # bound methods for the instance
#
# Person.do_work = lambda self:f"do work called from {self}"
#
# print(Person.__dict__)
# print(p.do_work)
#
# # on the other hand, if function is added to instance directly, it does not get bound
#
# p.do_work2 = lambda *args: f"do_work2 called with {args}"
#
# print(p.do_work2)
# print(p.__dict__)



# # INITIALIZING AND INSTANTIATING
#
# # when ins created, firstly it is instantiated then its namespace is initiated (__dict__ returns {})
# # dunder __init__ is called as a method bound to intercept the newly created instance (but obj already
# # instantiated and initialized)
#
#
#
# class MyNewClass():
#
#     def say_hello():
#         print("ello")
#
#     # these are instance attributes
#     def __init__(self, version):
#         self.version = version
#
# newobj = MyNewClass(3.8)
# print(newobj.version)
#
# # does the same thing as above
# MyNewClass.__init__(newobj, 3.7)
# print(newobj.version)
#
# # __init__ becomes a bound method when called from the obj instance, just like say_hello
# # bound methods receive obj instance as first parameter, so if self not defined, function returns error
#
# print(newobj.say_hello)
# print(newobj.__init__)
# print(newobj.__dict__)
#
#
# # same thing wo the special dunder init
# class MyNewClass2():
#
#     def init(self, version):
#         self.version = version
#
# abc = MyNewClass2()
# abc.init(4.5)
# print(abc.__dict__)



# # BINDING FUNCTIONS TO OBJ AT RUNTIME
# # normally when function defined on obj at runtime, Python does not know it is bound, so cant have
# # access to object`s namespace. (only bound if defined in class)
#
# from types import MethodType
#
# class MyClass():
#     language = "python"
#
#     def say_hello_from_class():
#         print("hello")
#
# obj = MyClass()
#
# # obj.say_hello = MethodType(lambda self: f"Hello {self.language}", obj)
#
# # self is by convention, can use anything
#
# obj.say_hello = MethodType(lambda anything: f"Hello {anything.language}", obj)
#
# print(obj.say_hello())
#
# # now it is a bound method of the instance object from MyClass
# print(obj.say_hello)
# print(obj.__dict__)
# print(obj.say_hello.__self__, obj.say_hello.__func__)
#
#
#
# setattr(obj, "_do_work", lambda : f"Hello")
#
# print(obj._do_work())



# # PROPERTIES (DIFF TO ATTRIBUTES)
# # PYTHON allows access to private instance attributes (unlike Java) but convention is to use single
# # underscore _ and use get/set method
#
# # also if we start with a class tht allows direct access to attribute, and need to change it later,
# # we will have to change the interface
#
# class Private():
#     # first set the value from init
#     def __init__(self, language):
#         self._language = language
#
#     def get_language(self):
#         return self._language
#
#     def set_language(self, value):
#         self._language = value
#
#
#
#
# # using get/set allows control over input
#
# a = Private("python")
#
# print(a.get_language())
# a.set_language("java")
# print(a.__dict__, a._language)
#
# # now i dont have direct access to a.language; need to use workaround get/set methods
# # solution is to create a property
#
#
# class PrivateProperty():
#     # first set the value from init
#     def __init__(self, language):
#         self._language = language
#
#     def get_language(self):
#         return self._language
#
#     def set_language(self, value):
#         self._language = value
#
#     # this is how property is created
#     language = property(fget=get_language, fset=set_language)
#
#
# # so we can start by only creating instance attributes and if we need to , modify the class and create property.
# # the interface (how that property is accessed in the code) would not change
# # i.e -> obj.language
#
# b = PrivateProperty("python")
#
# print(b.language)
# b.language = "java"
# print(b.__dict__, b.language)
#
# # why property is useful? because with direct access we cant control the values of attribute.
# # we can set a float value to language etc. so we use property and get/set to mimic private attribute
#
#
# b.__dict__["language"] = "java degil"
# # --> {'_language': 'java', 'language': 'java degil'}
# print(b.__dict__)
#
# print(b.language)
# # --> java
#
#
# # as seen above, even if we manually add language to dict,
# # PYTHON still recognizes that language is a property and uses get/set methods to read/write value to/from
# # _language


# # PROPERTY DECORATORS
#
# from math import pi
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self._area = None
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         # if radius value is set we invalidate our cached _area value
#         # we could make this more intelligent and see if the radius has actually changed
#         # but keeping it simple
#         self._area = None
#         # we could even add validation here, like value has to be numeric, non-negative, etc
#         self._radius = value
#
#     @property
#     def area(self):
#         if self._area is None:
#             # value not cached - calculate it
#             print('Calculating area...')
#             self._area = pi * (self.radius ** 2)
#         return self._area
#
#
# c = Circle(1)
# print(c.area)
# c.radius = 2
# print(c.area)


# # CLASS AND STATIC METHODS
#
# class MyClass():
#     abc = 1212
#
#     def hello():
#         print("hello")
#
#     def inst_hello(self):
#         print(f"hello from {self}")
#
#     @classmethod
#     def cls_hello(cls):
#         print(f"hello from {cls}")
#
# c = MyClass()
#
# print(MyClass.hello)
# >>> <function MyClass.hello at 0x000001829D179A68>
# MyClass.hello()
# >>> hello
#
#
# print(c.hello)
# >>> <bound method MyClass.hello of <__main__.MyClass object at 0x000001829D189C48>>
# c.hello()
# >>> TypeError: hello() takes 0 positional arguments but 1 was given
#
#
# print(MyClass.inst_hello)
# >>> <function MyClass.inst_hello at 0x000001C0F5989708>
# MyClass.inst_hello()
# >>> TypeError: inst_hello() missing 1 required positional argument: 'self'
#
# print(MyClass.cls_hello)
# >>> <bound method MyClass.cls_hello of <class '__main__.MyClass'>>
# MyClass.cls_hello()
# >>> hello from <class '__main__.MyClass'>
# print(c.cls_hello)
# >>> <bound method MyClass.cls_hello of <class '__main__.MyClass'>>
# c.cls_hello()
# >>> hello from <class '__main__.MyClass'>


# CLASS BODY SCOPE
# a func defined inside a class has a scope that is not the class but the nearest enclosing scope
# in this case the outer module
# so if we reference an attribute inside the function, we need to tell the function
# where to look for it (instance, class) otherwise it will look for it in the nearest enclosing scope

class Language():
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    FULL = f"{MAJOR}.{MINOR}.{REVISION}"

    @property
    def version(self):
        return f"{self.MAJOR}.{self.MINOR}.{self.REVISION}"

    @classmethod
    def cls_version(cls):
        return f"{cls.MAJOR}.{cls.MINOR}.{cls.REVISION}"

    @staticmethod
    def static_version():
        return f"{Language.MAJOR}.{Language.MINOR}.{Language.REVISION}"

l = Language()

print(Language.FULL, l.FULL)
print(l.version)
print(Language.cls_version())
print(Language.static_version())


MAJOR = 1
MINOR = 4
REVISION = 7

def gen_class():
    MAJOR = 21
    MINOR = 24
    REVISION = 27

    class Language2():
        MAJOR = 31
        MINOR = 34
        REVISION = 37

        @classmethod
        def version(cls):
            return f"{MAJOR}.{MINOR}.{REVISION}"


    return Language2

cls = gen_class()
print(type(cls))
# >>> <class 'type'>
print(cls.__dict__)

print(cls.version())
# >>> 21.24.27
# returned from the nearest enclosing scope, which is the gen_class() function
# if we had not had it, it would look for it in the module scope and return 1.4.7

# so basically this func cls.version is a closure, it is closing over the variables from outer scope

import  inspect
print(inspect.getclosurevars(cls.version))
# >>> ClosureVars(nonlocals={'MAJOR': 21, 'MINOR': 24, 'REVISION': 27}, globals={}, builtins={}, unbound=set())

class New:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

newname = New("qesj")

# newname.name = "qesh"

print(newname.__dict__)
print(newname.name)