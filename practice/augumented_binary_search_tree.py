class Node:
    def __init__(self, data, parent, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class AugumentedBST(object):
    def __init__(self):
        pass

    def add_nodes(self, root, val):
        if root is None:
            return Node(val)
        else:
            if val < root.data:
                root.left = self.add_nodes(root.left, val)
            elif val > root.data:
                root.right = self.add_nodes(root.right, val)
            else:
                pass
            return root

    def in_order_traversal(self, root):
        op = []
        if root:
            op.extend(self.in_order_traversal(root.left))
            op.append(root.data)
            op.extend(self.in_order_traversal(root.right))
        return op

    def create_bst_from_sorted_arr(self, ip_arr):
        if len(ip_arr) == 0:
            return
        mid_index = len(ip_arr) / 2
        mid_element = ip_arr[mid_index]
        root_node = Node(mid_element)
        root_node.left = self.create_bst_from_sorted_arr(ip_arr[:mid_index])
        root_node.right = self.create_bst_from_sorted_arr(ip_arr[mid_index + 1:])
        return root_node

sorted_arr = [i for i in range(8)]
bst = AugumentedBST()
root_node = bst.create_bst_from_sorted_arr(sorted_arr)
print bst.in_order_traversal(root_node)
print sorted_arr
assert bst.in_order_traversal(root_node) == sorted_arr