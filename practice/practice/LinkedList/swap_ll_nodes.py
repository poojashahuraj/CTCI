class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def add_node(self, val):
        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node
        return self.head

    def print_ll(self):
        node = self.head
        while node is not None:
            print str(node.data) + "->",
            node = node.next_node
        print

    def swap_node(self, x, y):
        """
        given node x and y swap them in linked list
        ip_ll: 1->2->3->4->5->6, x=2, y=5
        op: 1->5->3->4->2->6
        """
        # start with node
        cur_x = self.head
        cur_y = self.head
        prev_x = None
        prev_y = None

        if x == y:
            return
        while cur_x is not None and cur_x.data != x:
            prev_x = cur_x
            cur_x = cur_x.next_node

        while cur_y is not None and cur_y.data != y:
            prev_y = cur_y
            cur_y = cur_y.next_node

        if cur_x.next_node is not None and cur_y.next_node is not None:
            temp = cur_x.next_node
            cur_x.next_node = cur_y.next_node
            cur_y.next_node = temp
        if prev_x is not None:
            prev_x.next_node = cur_y
        else:
            # means x was head of old ll, so make y as new head of list.
            self.head = cur_y

        if prev_y is not None:
            prev_y.next_node = cur_x
        else:
            # y was head of old linkedlist, so make x as head of new linked list.
            self.head = cur_x
        self.print_ll()
        # coroner cases : what is x and y are head or tail
        # what if x and y are same nodes
        # what is x and y are not present in ll.

    @staticmethod
    def merge_two_sorted_ll(head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        s = temp_node = Node(-1)
        while not (head1 is None or head2 is None):
            if head1.data < head2.data:
                # remember current low-node
                current_low_node = head1
                # follow ->next
                head1 = head1.next_node
            else:
                # remember current low-node
                current_low_node = head2
                # follow ->next
                head2 = head2.next_node
            # consider this as appending at the tail of linkedlist
            temp_node.next_node = current_low_node
            # and make sure we also advance the temp
            temp_node = temp_node.next_node
        # once we are done iterating through one list append the remianing list to the node
        temp_node.next_node = head1 or head2
        return s.next_node


head = Node(1)
ll = LinkedList(head)
for i in range(2, 10):
    ll.add_node(i)
ll.print_ll()
ll.swap_node(3, 7)

print "Merge two sorted linked list"
ll1 = LinkedList(Node(6))
for i in (4, 2, 0):
    ll1.add_node(i)
print "First linked list:"
ll1.print_ll()

ll2 = LinkedList(Node(7))
for i in (5, 3, 1):
    ll2.add_node(i)
print "Second linked list:"
ll2.print_ll()

new_node = Node(-1)
new_ll = LinkedList(new_node)
head = new_ll.merge_two_sorted_ll(ll1.head, ll2.head)
print "new merged linked list is:"
while head is not None:
    print str(head.data) + "->",
    head = head.next_node
