import abc
from aetypes import Enum


class AbstractBaseClass(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def foo(self):
        pass

    @abc.abstractproperty
    def bar(self):
        pass


class ConcreteClass(AbstractBaseClass):

    def __init__(self, foo, bar):
        self._foo = foo
        self._bar = bar

    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, value):
        self._foo = value

    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, value):
        self._bar = value


class EmployeeTypes(Enum):
    manager = 1
    secretary = 2
    peon = 3


p = ConcreteClass("f", "b")
print p.bar
print p.foo
p.bar = "b1"
p.foo = "f1"
print p.bar
print p.foo
print EmployeeTypes.manager