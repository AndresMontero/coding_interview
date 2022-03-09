# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def aux(tree, min_val, max_val):
    if tree is None:
        return True
    if tree.value < min_val or tree.value >= max_val:
        return False

    remainder_left = aux(tree.left, min_val, tree.value)
    remainder_right = aux(tree.right, tree.value, max_val)

    return remainder_left and remainder_right


def validateBst(tree):
    # Time O(n) where n is the number of nodes
    # Space O(d) where d is the depth of the tree
    # Write your code here.
    return aux(tree, float('-inf'), float('inf'))


if __name__ == '__main__':
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    print(validateBst(root))
