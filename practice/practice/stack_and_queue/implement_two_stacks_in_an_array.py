class Stack(object):
    def __init__(self, size):
        self.size = size
        self.top1 = -1
        self.top2 = self.size
        self.stack = [None]*size

    def push1(self,val):
        if self.top2-1 > self.top1:
            self.top1 += 1
            self.stack[self.top1] = val

        else:
            print "Stackoverflow"
            raise SystemError

    def push2(self, val):
        if self.top2 - 1 > self.top1:
            self.top2 -= 1
            self.stack[self.top2] = val
        else:
            print "stackoverflow"
            raise -1

    def pop1(self):
        if self.top1 > -1:
            val = self.stack.pop(self.top1)
            self.top1 -= 1
            return val
        else:
            print "Underflow error"
            raise  -1

    def pop2(self):
        if self.top2 < self.size:
            val = self.stack.pop(self.top2)
            self.top2 += 1
            return val
        else:
            print "stack 2 is empty"
            return -1


ts = Stack(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))