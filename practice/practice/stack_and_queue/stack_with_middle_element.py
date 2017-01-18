"""
Design a stack with operations on middle element
How to implement a stack which will support following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
Push and pop are standard stack operations.

Hint: use doubly link list ,move pointer up and down with push and pop
"""
import sys

class Node(object):
    def __init__(self, value, next_node=None, previous_node=None):
        self.data = value
        self.next_node = next_node
        self.previous_node = previous_node


class LinkedList(object):
    def __init__(self, size, head):
        self.size = size-1 # one head i already added in linked list
        self.head = head

    def push(self, value):
        if self.size > 0:
            new_node = Node(value)
            head_node = self.head
            new_node.next_node = head_node
            head_node.previous_node = new_node
            self.head = new_node
            self.size -= 1
            return self.head
        else:
            print "stack over flow error."
            sys.exit(1)

    def pop(self):
        self.size +=1
        head_node = self.head
        self.head = head_node.next_node
        return head_node.data


head = Node(5)
ll = LinkedList(5, head)
for i in range(4,0,-1):
    head = ll.push(i)
print "Head is at {}".format(head.data)
print "Popped {}".format(ll.pop())
print "Popped {}".format(ll.pop())
print "Pushed {}".format(ll.push(11).data)
print "Popped {}".format(ll.pop())
