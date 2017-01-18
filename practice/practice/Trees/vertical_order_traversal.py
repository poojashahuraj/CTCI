from collections import defaultdict


class Node(object):
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.left = left
        self.right =right


class BinaryTree(object):
    def __init__(self):
        pass

    def add_node(self, root, value):
        if root is None:
            new_node = Node(value)
            return new_node
        if root.data > value:
            root = self.add_node(root.left, value)
        elif root.data < value:
            root = self.add_node(root.right, value)
        return root

    def create_bt_from_sorted_arr(self, arr):
        if len(arr) == 0:
            return
        mid_index = len(arr)//2
        mid_element = arr[mid_index]
        node = Node(mid_element)
        node.left = self.create_bt_from_sorted_arr(arr[0:mid_index])
        node.right = self.create_bt_from_sorted_arr(arr[mid_index+1:])
        return node

    def in_order_traversal(self, root):
        result = []
        if root:
            result.extend(self.in_order_traversal(root.left))
            result.append(root.data)
            result.extend(self.in_order_traversal(root.right))
        return result

    def left_edge(self, root):
        result = []
        if root:
            result.append(root.data)
            result.extend(self.left_edge(root.left))
        return result

    def right_edge(self, root):
        result = []
        if root:
            result.append(root.data)
            result.extend(self.right_edge(root.right))
        return result

    def leaves(self, root):
        result = []
        if root:
            if root.left is None and root.right is None:
                result.append(root.data)
            else:
                result.extend(self.leaves(root.left))
                result.extend(self.leaves(root.right))
        return result

    def get_height(self, root):
        if root is None:
            return 0
        ht = 1+max(self.get_height(root.left), self.get_height(root.right))
        return ht

    def level_order_travesal(self, root, level):
        if root is None:
            return []
        if level == 1:
            return [root.data]
        else:
            op = []
            op.extend(self.level_order_travesal(root.left, level-1))
            op.extend(self.level_order_travesal(root.right, level-1))
            return op

    def getVerticalOrder(self, root, hd, map_dict):
        if root is None:
            return
        map_dict[hd].append(root.data)
        self.getVerticalOrder(root.left, hd - 1, map_dict)
        self.getVerticalOrder(root.right, hd + 1, map_dict)

    def printVerticalOrder(self,root):
        m = defaultdict(list)
        hd = 0
        self.getVerticalOrder(root, hd, m)

        # Traverse the map and print nodes at every horizontal
        # distance (hd)
        for index, value in enumerate(sorted(m)):
            for i in m[value]:
                print i,


ip = [i for i in range(10)]
bt = BinaryTree()
r1 = bt.create_bt_from_sorted_arr(ip)
assert bt.in_order_traversal(r1) == ip
print bt.level_order_travesal(r1, 1)
print bt.level_order_travesal(r1, 2)
print bt.level_order_travesal(r1, 3)
print bt.level_order_travesal(r1, 4)
print "Vertical order traversal:"
bt.printVerticalOrder(r1)
print ""
print "Left edge is:{}".format(bt.left_edge(r1))
print "Right edge is:{}".format(bt.right_edge(r1))
print "Leaves of binary tree are {}".format(bt.leaves(r1))
