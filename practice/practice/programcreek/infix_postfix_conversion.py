# Python program to convert infix expression to postfix


class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.weight = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isCharacter(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        try:
            operator_wt = self.weight[i]
            stack_top_wt = self.weight[self.peek()]
            return True if operator_wt <= stack_top_wt else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        for i in exp:
            if self.isCharacter(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while (not self.isEmpty()) and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()

            else:
                while not self.isEmpty() and self.notGreater(i):
                    self.output.append(self.pop())
                self.push(i)

        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        print "".join(self.output)


# Driver program to test above function
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)