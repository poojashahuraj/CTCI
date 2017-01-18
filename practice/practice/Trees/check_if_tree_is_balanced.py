# coding=utf-8
"WAP to check if given tree is balanced or not"


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        pass

    def add_node(self, root_node, value):
        if root_node is None:
            return Node(value)
        else:
            if value > root_node.data:
                root_node.right = self.add_node(root_node.right, value)
            elif value < root_node.data:
                root_node.left = self.add_node(root_node.left, value)
            else:
                print "{} is already in tree, do nothing".format(value)
        return root_node

    def create_binary_tree_from_sorted_arr(self, ip_arr):
        if len(ip_arr) < 1:
            return
        mid_index = len(ip_arr) / 2
        mid_element = ip_arr[mid_index]
        node = Node(mid_element)
        node.left = self.create_binary_tree_from_sorted_arr(ip_arr[0:mid_index])
        node.right = self.create_binary_tree_from_sorted_arr(ip_arr[mid_index + 1:])
        return node

    def get_smallest_element(self, root):
        current_node = root
        result_a = []
        while current_node.left is not None:
            result_a.append(current_node.data)
            current_node = current_node.left
        result_a.append(current_node.data)
        return result_a

    def get_largest_element(self, root):
        current_node = root
        result_arr = []
        while current_node.right is not None:
            result_arr.append(current_node.data)
            current_node = current_node.right
        result_arr.append(current_node.data)
        return result_arr

    def check_if_binary_tree_is_balanced(self, root):

        """
        1) Left subtree of T is balanced
        2) Right subtree of T is balanced
        3) The difference between heights of left subtree and right subtree is not more than 1.
        """
        return self.isBalancedInt(root) >= 0

    def isBalancedInt(self, root):
        if root is None:
            return 0
        left_height = self.isBalancedInt(root.left)
        right_height = self.isBalancedInt(root.right)
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def get_height(self, root):
        if root is None:
            return 0
        return 1+max(self.get_height(root.left), self.get_height(root.right))

    def in_order_traversal(self, root):
        result_arr = []
        if root:
            # for in order traversal we have left -> root-> right
            result_arr.extend(self.in_order_traversal(root.left))
            result_arr.append(root.data)
            result_arr.extend(self.in_order_traversal(root.right))
        return result_arr

    def pre_order_traversal(self, root):
        result_arr = []
        if root:
            # for pre order traversal we have root -> left -> right
            result_arr.append(root.data)
            result_arr.extend(self.in_order_traversal(root.left))
            result_arr.extend(self.in_order_traversal(root.right))
        return result_arr

    def post_order_traversal(self, root):
        result_arr = []
        if root:
            # for in order traversal we have left -> right -> root
            result_arr.extend(self.in_order_traversal(root.left))
            result_arr.extend(self.in_order_traversal(root.right))
            result_arr.append(root.data)
        return result_arr

    def get_path_for_given_val(self, root, value):
        current_node = root
        result = []
        while current_node is not None:
            result.append(current_node.data)
            if value > current_node.data:
                current_node = current_node.right
            elif value < current_node.data:
                current_node = current_node.left
            else:
                break
        if current_node is None:
            print "{} is not present in binary tree. Search path {}.".format(value, result)
            return -1
        return result

    """
    Write an algorithm to  nd the ‘next’ node (e.g., in-order successor) of a
    given node in a binary search tree where each node has a link to its parent.
    """
    def find_next_node(self, root, value):
        if root is None:
            return
        result_arr = []
        result_arr.extend(self.find_next_node(root.left, value))
        result_arr.append(root.data)
        result_arr.extend(self.find_next_node(root.right, value))
        return result_arr


if "__main__" == __name__:
    ip_arr = [i for i in range(10)]
    bt = BinaryTree()
    root = bt.create_binary_tree_from_sorted_arr(ip_arr)
    print bt.get_smallest_element(root)
    print bt.get_largest_element(root)
    print bt.check_if_binary_tree_is_balanced(root)
    assert bt.in_order_traversal(root) == ip_arr
    print bt.pre_order_traversal(root)
    print bt.post_order_traversal(root)
    print bt.get_path_for_given_val(root, 13)
    for i in ip_arr:
        print "Traversal path for {}:{}".format(i, bt.get_path_for_given_val(root, i))