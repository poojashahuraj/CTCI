import abc
class AbstractBaseClass(object):
    @abc.abstractproperty
    def size(self):
        pass

    def say_something(self):
        raise NotImplementedError

    def no_need_to_override(self):
        print "from abstract class."


class ChildClass(AbstractBaseClass):
    def size(self):
        return 1

    def say_something(self):
        print "saying from child class"


a = AbstractBaseClass()
a.no_need_to_override()
c = ChildClass()
print c.size()
c.say_something()
c.no_need_to_override()

from collections import deque
items = deque([1, 2, 3, 4])
items.append(3) # deque == [1, 2, 3]
items.rotate(1) # The deque is now: [3, 1, 2]
print items

items.rotate(-1) # Returns deque to original state: [1, 2, 3]
print items

item = items.popleft() # deque == [2, 3]
