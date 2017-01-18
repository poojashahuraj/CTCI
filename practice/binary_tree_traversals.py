class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left


class BinaryTreeTraversal(object):
    def __init__(self):
        pass

    def add_node(self, root, value):
        if root is None:
            return Node(value)
        else:
            if value < root.data:
                root.left = self.add_node(root.left, value)
            elif value > root.data:
                root.right = self.add_node(root.right, value)
            else:
                print "{} is already present in node".format(value)
            return root

    def pre_order_recursive(self, root):
        traverse_path = []
        if root is not None:
            traverse_path.append(root.data)
            traverse_path.extend(self.pre_order_recursive(root.left))
            traverse_path.extend(self.pre_order_recursive(root.right))
        return traverse_path

    def post_order_recursive(self, root):
        traverse_path = []
        if root:
            traverse_path.extend(self.post_order_recursive(root.left))
            traverse_path.extend(self.post_order_recursive(root.right))
            traverse_path.append(root.data)
        return traverse_path

    def in_order_recursive(self, root):
        traverse_path = []
        if root:
            traverse_path.extend(self.in_order_recursive(root.left))
            traverse_path.append(root.data)
            traverse_path.extend(self.in_order_recursive(root.right))
        return traverse_path

    def pre_order_iterative(self, root):
        stack = [root]
        traverse_path = []
        while len(stack) > 0:
            n = stack.pop()
            traverse_path.append(n.data)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
        return traverse_path


root_node = Node(4)
bt = BinaryTreeTraversal()
for i in [4, 2, 6, 1, 3, 5, 7]:
    bt.add_node(root_node, i)
assert bt.pre_order_recursive(root_node) == bt.pre_order_iterative(root_node)
print bt.pre_order_iterative(root_node)
print bt.post_order_recursive(root_node)
print bt.in_order_recursive(root_node)


# Create a balanced binary search tree from a sorted array given.
# e.g. [1,2,3,4,5,6,7,8]


class BalancedBinarySearchTree(object):
    def __init__(self):
        pass

    def convert_to_bst(self, sortedlist):
        if len(sortedlist) == 0:
            return None
        mid = int(len(sortedlist) / 2)
        root = Node(sortedlist[mid])
        root.left = self.convert_to_bst(sortedlist[:mid])
        root.right = self.convert_to_bst(sortedlist[mid + 1:])
        return root

    def in_order_traversal(self, root_node):
        result = []
        if root_node is not None:
            result.extend(self.in_order_traversal(root_node.left))
            result.append(root_node.data)
            result.extend(self.in_order_traversal(root_node.right))
        return result

    def max_depth(self, root_node):
        if root_node is None:
            return 0
        l_depth = self.max_depth(root_node.left)
        r_depth = self.max_depth(root_node.right)
        if l_depth > r_depth:
            return l_depth+1
        else:
            return r_depth+1

bbt = BalancedBinarySearchTree()
sorted_arr = [i for i in range(12)]
root_node = bbt.convert_to_bst(sorted_arr)
assert bbt.in_order_traversal(root_node) == sorted_arr
assert bbt.max_depth(root_node) == 4, "{}".format(bbt.max_depth(root_node))
btt = BinaryTreeTraversal()

root_node = Node(11)
for i in range(10,1,-1):
    root_node = btt.add_node(root_node,i)
print bbt.max_depth(root_node)