class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def add_node(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def print_ll(self):
        current_node = self.head
        op = []
        while current_node.next_node is not None:
            op.append(current_node.data)
            current_node = current_node.next_node
        op.append(current_node.data)
        a = ''
        for j in op:
            a += str(j)+"->"
        print a
        return op

    def find_middle_of_ll(self):
        p1 = self.head
        p2 = self.head
        while p2 is not None and p2.next_node is not None:
            p1 = p1.next_node
            p2 = p2.next_node.next_node
        return p1.data

head = Node(7)
ll = LinkedList(head)
for i in range(6, -1, -1):
    ll.add_node(i)
ll.print_ll()
print ll.find_middle_of_ll()