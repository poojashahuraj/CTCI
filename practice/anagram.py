class Anagram(object):
    def __init__(self, input_str1, input_str2):
        self._input1 = input_str1.lower().replace(" ","")
        self._input2 = input_str2.lower().replace(" ", "")

    def run(self):
        if sorted(list(self._input1)) == sorted(list(self._input2)):
            print self._input1, self._input2
            return True
        else:
            return False
a = Anagram("pooooja", "oopja")
b = Anagram("iceman", "mancei")
c = Anagram("Moon starter", "Astronome")
d = Anagram("apple", "pleap")

print a.run()
print "==============="
print b.run()
print "==============="
print c.run()
print "==============="
print d.run()
print "==============="