# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    # Write your code here.

    return get_height(tree)[0]


def get_height(tree):
    # Time O(n)
    # Space O(1)
    if tree is None:
        return [True, -1]

    left_tree_info = get_height(tree.left)
    right_tree_info = get_height(tree.right)
    currentHeight = 1 + max(left_tree_info[1], right_tree_info[1])

    if left_tree_info[0] and right_tree_info[0] and abs(left_tree_info[1] - right_tree_info[1]) <= 1:
        return [True, currentHeight]

    return [False, 0]

if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)
    root.left.right.left = BinaryTree(7)
    root.left.right.right = BinaryTree(8)
    print(heightBalancedBinaryTree(root))
