# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def inOrderTraversal(tree, array):
    if tree.left:
        inOrderTraversal(tree.left, array)

    array.append(tree.value)

    if tree.right:
        inOrderTraversal(tree.right, array)

    return array


def findSuccessor(tree, node):
    # Write your code here.
    node_value = node.value
    array = []
    nums = inOrderTraversal(tree, array)
    for i in range(len(nums) - 1):
        if nums[i] == node_value:
            return nums[i + 1]

    return None


def findSuccessor_2(tree, node):
    # Time O(d) deep of the tree
    # Space O(1)
    # Write your code here.

    if node.right:
        return get_left_most_child(node.right)

    return get_right_most_parent(node)


def get_left_most_child(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left

    return currentNode


def get_right_most_parent(node):
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    return currentNode.parent

if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.parent = root
    root.right = BinaryTree(3)
    root.right.parent = root
    root.left.left = BinaryTree(4)
    root.left.left.parent = root.left
    root.left.right = BinaryTree(5)
    root.left.right.parent = root.left
    root.left.left.left = BinaryTree(6)
    root.left.left.left.parent = root.left.left
    node = root.left.right
    print(findSuccessor(root, node))
    print(findSuccessor_2(root, node).value)
