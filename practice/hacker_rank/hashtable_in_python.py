
class Hashtable(object):
    def __init__(self, size):
        self._size = size
        self.list = [None]*size

    def hashfunction(self, key):
        return key%self._size

    def put(self, key, value):
        index = self.hashfunction(key)
        self.list[index] = value

    def get(self, key):
        index = self.hashfunction(key)
        return self.list[index]
ht = Hashtable(10)
ht.put(1,"apple")
print ht.get(1)
ht.put(11, "banana")

print ht.get(1)
print ht.get(11)


class First(object):
    def __init__(self):
        print "first"


class Second(object):
    def __init__(self):
        print "second"


class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print "that's it"

Third()


class NewThird(Second, First):
    def __init__(self):
        super(NewThird, self).__init__()
        print "that's it"

NewThird()


def try_to_change_string_reference(outer_string):
    print 'got', outer_string
    outer_string = 'OUTER'
    print 'set to', outer_string

outer_string = 'OUTER'

print 'before, outer_string =', outer_string
try_to_change_string_reference(outer_string)
print 'after, outer_string =', outer_string