class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def __init__(self):
        pass

    def add_node(self, root, value):
        if root is None:
            return Node(value)

        if value > root.data:
            node = self.add_node(root.right, value)
        elif value < root.data:
            node = self.add_node(root.left, value)
        else:
            print "Node already exists in tree"
            return
        return node

    def create_bt_from_sorted_arr(self, arr):
        if len(arr) == 0:
            return
        mid_index = len(arr)//2
        mid_element = arr[mid_index]
        node = Node(mid_element)
        node.left = self.create_bt_from_sorted_arr(arr[0:mid_index])
        node.right = self.create_bt_from_sorted_arr(arr[mid_index+1:])
        return node

    def pre_order(self, root):
        op = []
        if root:
            op.append(root.data)
            op.extend(self.pre_order(root.left))
            op.extend(self.pre_order(root.right))
        return op

    def post_order(self, root):
        op = []
        if root:
            op.extend(self.post_order(root.left))
            op.extend(self.post_order(root.right))
            op.append(root.data)
        return op

    def in_order(self, root):
        op = []
        if root:
            op.extend(self.in_order(root.left))
            op.append(root.data)
            op.extend(self.in_order(root.right))
        return op

    def height_of_node(self, node):
        if node is None:
            return 0
        left_height = self.height_of_node(node.left)
        right_height = self.height_of_node(node.right)
        return max(left_height, right_height)+1

    def printGivenLevel(self, root, level):
        if root is None:
            return []
        op =[]
        if level == 1:
            op.append(root.data)
            # print "%d" % root.data,
        elif level > 1:
            op.extend(self.printGivenLevel(root.left, level - 1))
            op.extend(self.printGivenLevel(root.right, level - 1))
        return op

    def printLevelOrder(self, root):
        h = self.height_of_node(root)
        for i in range(1, h + 1):
            self.printGivenLevel(root, i)

arr = [i for i in range(10)]
a = BinarySearchTree()
root_node = a.create_bt_from_sorted_arr(arr)
assert a.in_order(root_node) == arr
print "Height of tree is:", a.height_of_node(root_node)
print "Level 1:", a.printGivenLevel(root_node, 1)
print "Level 2:", a.printGivenLevel(root_node, 2)
print "Level 3:", a.printGivenLevel(root_node, 3)
print "Level 4:", a.printGivenLevel(root_node, 4)
