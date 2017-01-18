# Implement a stack using two queues


class StackWithTwoQueues(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, value):
        self.queue1.append(value)

    def pop(self):
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        op = self.queue1.pop(0)
        assert len(self.queue1) == 0
        temp = self.queue1
        self.queue1 = self.queue2
        self.queue2 = temp
        return op

s = StackWithTwoQueues()
for i in range(10):
    s.push(i)
assert s.pop() == 9
s.push(11)
assert s.pop() == 11