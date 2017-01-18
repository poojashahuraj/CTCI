# coding=utf-8
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class DuplicateLinkedList(object):
    def __init__(self, head):
        self.head = head

    def add_node(self, value):
        current_node = self.head
        new_node = Node(value)
        new_node.next_node = current_node
        self.head = new_node

    def get_ll(self):
        result_arr = []
        current_node = self.head
        while current_node.next_node is not None:
            result_arr.append(current_node.data)
            current_node = current_node.next_node
        result_arr.append(current_node.data)
        return result_arr

    def print_ll(self):
        result_arr = self.get_ll()
        op = ""
        for i in result_arr:
            op = op + str(i)+ "->"
        print op

    def delete_node(self, value):
        """
        If value given is last node value then you can not delete it with this method
        :param value:
        :return:
        """
        current_node = self.head
        while current_node.next_node is not None:
            if current_node.data == value:
                current_node.data = current_node.next_node.data
                current_node.next_node = current_node.next_node.next_node
                break
            else:
                current_node = current_node.next_node

    def remove_duplicate_node(self):
        n_list = self.get_ll()
        from collections import defaultdict
        dict_a = defaultdict(int)
        for i in n_list:
            dict_a[i] += 1
        for key, value in dict_a.iteritems():
            if value > 1:
                for i in range(value-1):
                    self.delete_node(key)
        self.print_ll()

    def add_two_ll(self):
        """
        You have two numbers represented by a linked list, where each node contains a sin- gle digit.
        The digits are stored in reverse order, such that the 1’s digit is at the head of the list.
        Write a function that adds the two numbers and returns the sum as a linked list.
        """
        pass

        def find_start_of_circular_ll(self):
            p1 = self.head
            p2 = self.head
            while p1.data != p2.data and p1 != self.head:
                p1 = p1.next_node
                p2 = p2.next_node.next_node

            # Move P1 back to head node. Keep P2 at meeting node only
            p1 = self.head

            # now move p1 and p2 with same speed.
            while p1.data != p2.data and p1 != self.head:
                p1 = p1.next_node
                p2 = p2.next_node.next_node
            return p2.data


if __name__ == '__main__':
    root_node = Node(9)
    ll = DuplicateLinkedList(root_node)
    for i in [9,9,9,9,9,8,7,7,7,6,5,4,3,2,1]:
        ll.add_node(i)
    ll.print_ll()
    ll.remove_duplicate_node()
    ll.print_ll()
    # find the start of circular list
    root_node = Node(1)
    circular_ll = DuplicateLinkedList(root_node)
