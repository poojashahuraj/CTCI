"""
Remove duplicate element from a linked list.
"""

from collections import defaultdict


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class RemoveDuplicateLL(object):
    def __init__(self, head):
        self.head = head

    def add_node(self, val):
        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node
        return self.head

    def print_ll(self):
        current_node = self.head
        op_arr = []
        op = ''
        while current_node.next_node is not None:
            op_arr.append(current_node.data)
            op += str(current_node.data) + "->"
            current_node = current_node.next_node
        op_arr.append(current_node.data)
        op = op + str(current_node.data) + "->"
        print op
        return op_arr

    def remove_dup_node(self):
        dict_a = defaultdict(int)
        current_node = self.head
        while current_node is not None:
            if dict_a[current_node.data] == 0:
                dict_a[current_node.data] += 1
                current_node = current_node.next_node
            else:
                # occurrences of the data with same node happened before so remove that elements
                current_node.data = current_node.next_node.data
                current_node.next_node = current_node.next_node.next_node


if __name__ == "__main__":
    first_node = Node(11)
    rl = RemoveDuplicateLL(first_node)
    for i in [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 8, 9, 9]:
        rl.add_node(i)
    print "Linked list before deleting duplicates."
    rl.print_ll()
    print "Linked list after deleting duplicates."
    rl.remove_dup_node()
    rl.print_ll()
