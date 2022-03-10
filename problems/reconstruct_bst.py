# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, root_idx):
        self.root_idx = root_idx


def aux(lower, upper, array, tree):
    if tree.root_idx == len(array):
        return None

    root_value = array[tree.root_idx]

    if root_value < lower or root_value >= upper:
        return None

    tree.root_idx += 1
    left_tree = aux(lower, root_value, array, tree)
    right_tree = aux(root_value, upper, array, tree)

    return BST(root_value, left_tree, right_tree)


def reconstructBst(preOrderTraversalValues):
    # Write your code here.

    tree_info = TreeInfo(0)

    return aux(float('-inf'), float('inf'), preOrderTraversalValues, tree_info)

if __name__ == '__main__':
    preOrderTraversalValues = [10, 4, 2, 1, 3, 17, 19, 18]
    tree = BST(10)
    tree.left = BST(4)
    tree.left.left = BST(2)
    tree.left.left.left = BST(1)
    tree.left.right = BST(3)
    tree.right = BST(17)
    tree.right.right = BST(19)
    tree.right.right.left = BST(18)
    print(reconstructBst(preOrderTraversalValues))
