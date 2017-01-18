"""
Maintain head pointer in through out linkedlist class.
In Binary tree you do not need to maintain root node through out the class, every time you add node pass root Node
"""


class Node(object):
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left


class BinaryTree(object):
    def __init__(self):
        pass

    def insert_node(self, node, value):
        if node is None:
            return Node(value)
        else:
            if value < node.data:
                node.left = self.insert_node(node.left, value)
            elif value > node.data:
                node.right = self.insert_node(node.right, value)
            else:
                pass
            return node

    def get_traversing_path(self, node, value):
        current_node = node
        result_arr = []
        while current_node is not None:
            result_arr.append(current_node.data)
            if value < current_node.data:
                current_node = current_node.left
            elif value > current_node.data:
                current_node = current_node.right
            else:
                break
        return result_arr

    # root-> left -> right
    def pre_order_traversal(self, root):
        result_arr = []
        if root is not None:
            result_arr.append(root.data)
            result_arr.extend(self.pre_order_traversal(root.left))
            result_arr.extend(self.pre_order_traversal(root.right))
        return result_arr

    # left->root->right
    def in_order_traversal(self, root):
        result_arr = []
        if root is not None:
            result_arr.extend(self.in_order_traversal(root.left))
            result_arr.append(root.data)
            result_arr.extend(self.in_order_traversal(root.right))
        return result_arr

    # left -> right -> root
    def post_order_traversal(self, root):
        result_arr = []
        if root is not None:
            result_arr.extend(self.post_order_traversal(root.left))
            result_arr.extend(self.post_order_traversal(root.right))
            result_arr.append(root.data)
        return result_arr


bt = BinaryTree()
root = Node(8)
for i in [8, 4, 6, 2, 1, 3, 5]:
    bt.insert_node(root, i)
for i in [8, 4, 6, 2, 1, 3, 5]:
    print "{} : {}".format(i, bt.get_traversing_path(root, i))

bt = BinaryTree()
root = Node(4)
for j in [2, 6, 1, 3, 5, 7]:
    bt.insert_node(root, j)
print "-------------------------------"
print "In order : {}".format(bt.in_order_traversal(root))
print "Pre order : {}".format(bt.pre_order_traversal(root))
print "Post order : {}".format(bt.post_order_traversal(root))
print "-------------------------------"
