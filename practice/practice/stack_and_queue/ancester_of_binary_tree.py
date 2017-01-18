"""
Print ancester of a given binary tree
solution 1: Lets use level order traversal
"""
from collections import defaultdict


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class BinaryTree(object):
    def __init__(self):
        pass

    def add_node(self,root, val):
        if root is None:
            return Node(val)
        else:
            if val > root.data:
                self.add_node(root.right, val)
            else:
                self.add_node(root.left, val)
        return root

    def create_tree_from_sorted_arr(self, arr):
        if len(arr) == 0:
            return
        mid_index = len(arr)//2
        root = Node(arr[mid_index])
        root.left = self.create_tree_from_sorted_arr(arr[0:mid_index])
        root.right = self.create_tree_from_sorted_arr(arr[mid_index+1:])
        return root

    def pre_order_traversal(self, root):
        result = []
        if root is not None:
            result.extend(self.pre_order_traversal(root.left))
            result.append(root.value)
            result.extend(self.pre_order_traversal(root.right))
        return result

    def post_order_traversal(self, root):
        result = []
        if root is not None:
            result.extend(self.post_order_traversal(root.left))
            result.extend(self.post_order_traversal(root.right))
            result.append(root.value)
        return result

    def get_height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def get_nodes_at_given_level(self, root, level):
        if root is None:
            return []
        if level == 1:
            return [root.value]
        else:
            result = []
            result.extend(self.get_nodes_at_given_level(root.left, level-1))
            result.extend(self.get_nodes_at_given_level(root.right, level-1))
            return result

    def level_order_traversal(self, root):
        ht = self.get_height(root)
        for i in range(1, ht+1):
            print "At level {}, nodes are {}.".format(i, self.get_nodes_at_given_level(root, i))
        return

    def vertical_traversal(self, root):
        # hd stand for horizontal distance, 0 being root
        hd = 0
        # this dictionary stores node values at each vertical axis. we assume that root is zero and
        # left is minus and right is plus.
        dict_a = defaultdict(list)
        return self.vertical_traversal_helper(root, hd, dict_a)

    def vertical_traversal_helper(self, root, hd, dict_a):
        if root is None:
            return
        dict_a[hd].append(root.value)
        self.vertical_traversal_helper(root.left, hd-1, dict_a)
        self.vertical_traversal_helper(root.right, hd+1, dict_a)
        return dict_a

    def bottom_view(self, root):
        """
        Logic is simple just show last element from each vertical traversal array
        """
        dict_a = self.vertical_traversal(root)
        op = []
        for i in sorted(dict_a.keys()):
            op.append(dict_a[i][-1])
        return op

    def top_view(self, root):
        """
        Logic is simple just show first element from each vertical traversal array
        """
        dict_a = self.vertical_traversal(root)
        op = []
        for i in sorted(dict_a.keys()):
            op.append(dict_a[i][0])
        return op


sorted_arr = [i for i in range(10)]
bt = BinaryTree()
root = bt.create_tree_from_sorted_arr(sorted_arr)
print root.value
assert bt.pre_order_traversal(root) == sorted_arr
print "Post order traversal of binary tree is {}.".format(bt.post_order_traversal(root))
print "Height of the binary tree is {}".format(bt.get_height(root))
bt.level_order_traversal(root)
print bt.vertical_traversal(root)
print "Bottom view of tree is {}.".format(bt.bottom_view(root))
print "Top view of tree is {}.".format(bt.top_view(root))