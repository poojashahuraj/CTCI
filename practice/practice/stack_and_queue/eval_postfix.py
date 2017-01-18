class Postfix(object):
    def __init__(self, length):
        self.length = length
        self.stack = [-1]
        self.top = -1

    def push(self, val):
        self.stack.append(val)
        self.top += 1

    def pop(self):
        if not self.isempty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "$"

    def peek(self):
        return self.stack[-1]

    def isempty(self):
        if self.peek() == -1:
            return True
        else:
            return False

    def evaluate_exp(self, exp):
        for index, value in enumerate(exp):
            if value.isdigit():
                self.push(value)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval("{}{}{}".format(val2,value,val1))))
        return int(self.pop())



exp = "231*+9-"
s = Postfix(len(exp))
print s.evaluate_exp(exp)