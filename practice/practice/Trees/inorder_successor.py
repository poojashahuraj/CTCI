# Python program to find the inroder successor in a BST
# A binary tree node
from collections import defaultdict


class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BST(object):
    def __init__(self):
        pass

    def add_node(self, root, value):
        if root is None:
            return Node(value)
        if value < root.data:
            root.left = self.add_node(root.left, value)
        elif value > root.data:
            root.right = self.add_node(root.right, value)
        return root

    def in_order_traversal(self, root):
        result = []
        if root:
            result.extend(self.in_order_traversal(root.left))
            result.append(root.data)
            result.extend(self.in_order_traversal(root.right))
        return result

    def post_order_traversal(self, root):
        result = []
        if root:
            result.extend(self.post_order_traversal(root.left))
            result.extend(self.post_order_traversal(root.right))
            result.append(root.data)
        return result

    def pre_order_traversal(self, root):
        result = []
        if root:
            result.append(root.data)
            result.extend(self.pre_order_traversal(root.left))
            result.extend(self.pre_order_traversal(root.right))
        return result

    def level_order(self, root, level, op):
        if root is None:
            return
        if level == 0:
            op.append(root.data)
        else:
            self.level_order(root.left, level-1, op)
            self.level_order(root.right, level-1, op)
        return op

    def level_order_traversal(self, root):
        height = self.get_height(root)
        dict_a = {}
        for i in range(height):
            op = self.level_order(root, i, [])
            dict_a[i] = op
        return dict_a

    def get_height(self, root):
        if root is None:
            return 0
        left_ht = self.get_height(root.left)
        right_ht = self.get_height(root.right)
        return 1+max(left_ht, right_ht)

    def check_balanced(self, root):
        # each node's left subtree should be balaced
        # each node's right subtree should be balanced
        # two subtrees are balanced only if difference between their ht is < = 1
        if root is None:
            return 0
        left_ht = self.check_balanced(root.left)
        right_ht = self.check_balanced(root.right)
        if left_ht < 0 or right_ht <0 or abs(left_ht-right_ht) > 1:
            return -1
        else:
            return 1 + max(left_ht, right_ht)

    def create_bst_from_sorted_arr(self, ip_arr):
        if not ip_arr:
            return
        mid_index = len(ip_arr)//2
        mid_element = ip_arr[mid_index]
        root = Node(mid_element)
        root.left = self.create_bst_from_sorted_arr(ip_arr[0:mid_index])
        root.right = self.create_bst_from_sorted_arr(ip_arr[mid_index+1:])
        return root

    def vertical_order_traversal(self, root):
        dict_a = defaultdict(list)
        # consider root is at horizontal distance 0, when u go left reduce by, when u go right increase by 1
        hd = 0
        for i in sorted(self.vertical_order_traversal_helper(root, dict_a, hd)):
            print "{}:{}".format(i, dict_a[i])

    def vertical_order_traversal_helper(self, root, dict_a, hd):
        if not root:
            return
        dict_a[hd].append(root.data)
        self.vertical_order_traversal_helper(root.left, dict_a, hd-1)
        self.vertical_order_traversal_helper(root.right, dict_a, hd + 1)
        return dict_a

ip_arr = [i for i in range(10)]
b = BST()
root = b.create_bst_from_sorted_arr(ip_arr)
assert b.in_order_traversal(root) == ip_arr
print "Height of the tree is: {}. ".format(b.check_balanced(root))
print b.level_order_traversal(root)
print "Vertical order traversal is: {}".format(b.vertical_order_traversal(root))



def inOrderSuccessor(root, n):
    # so there are two scenarios such as:
    # if it has right child then left most element of right child.
    # if it does not have right child then parent
    # Step 1 of the above algorithm
    if n.right is not None:
        return minValue(n.right)

    # Step 2 of the above algorithm
    # traverse for parent until child is left child of parent
    p = n.parent
    while p is not None:
        # traverse back till parent until child is left child of parent.
        if n != p.right:
            break
        n = p
        p = p.parent
    return p


# Given a non-empty binary search tree, return the
# minimum data value found in that tree. Note that the
# entire tree doesn't need to be searched
def minValue(node):
    current = node

    # loop down to find the leftmost leaf
    while current is not None:
        if current.left is None:
            break
        current = current.left

    return current


# Given a binary search tree and a number, inserts a
# new node with the given number in the correct place
# in the tree. Returns the new root pointer which the
# caller should then use( the standard trick to avoid
# using reference parameters)
def insert(node, data):
    # 1) If tree is empty then return a new singly node
    if node is None:
        return Node(data)
    else:

        # 2) Otherwise, recur down the tree
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node

        # return  the unchanged node pointer
        return node


# Driver progam to test above function

root = None

# Creating the tree given in the above diagram
root = insert(root, 20)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10)
root = insert(root, 14)
temp = root.left.right.right

succ = inOrderSuccessor(root, temp)
if succ is not None:
    print "\nInorder Successor of %d is %d " \
          % (temp.data, succ.data)
else:
    print "\nInorder Successor doesn't exist"