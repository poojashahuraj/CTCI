"""
Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(),
isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack.
All these operations of SpecialStack must be O(1). To implement SpecialStack, you should only use standard Stack data
structure and no other data structure like arrays, list, .. etc.

Nothing fancy maintain one more stack of same size with min values.
"""
import sys


class SpecialStack(object):
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.aux_stack = []
        self.top = -1

    def isEmpty(self):
        if self.top >= 0:
            return False
        else:
            return True

    def isFull(self):
        if self.top >= self.size:
            print "Stack is full"
            sys.exit(1)

    def push(self, val):
        if not self.isEmpty():
            self.stack.append(val)
            min_val = self.aux_stack[-1]
            if val <= min_val:
                self.aux_stack.append(val)
            else:
                self.aux_stack.append(min_val)
            self.top += 1
        else:
            self.stack.append(val)
            self.aux_stack.append(val)
            self.top += 1

    def get_min_value(self):
        print self.aux_stack
        return self.aux_stack[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            self.aux_stack.pop()
            return self.stack.pop()

s = SpecialStack(5)
for i in [10, 22, 34, 14, 5, 67, 3, 2, 1]:
    s.push(i)
print s.get_min_value()
s.pop()
print s.get_min_value()
s.pop()
print s.get_min_value()
s.pop()
print s.get_min_value()
