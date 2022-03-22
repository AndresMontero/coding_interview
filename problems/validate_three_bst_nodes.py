# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_descendant(node_a, node_b):
    if node_a is None:
        return False

    if node_a == node_b:
        return True

    if node_b.value < node_a.value:
        return is_descendant(node_a.left, node_b)

    if node_b.value > node_a.value:
        return is_descendant(node_a.right, node_b)


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    # Time O(d)
    # Space O(d)
    if is_descendant(nodeTwo, nodeThree):
        if is_descendant(nodeOne, nodeTwo):
            return True
    elif is_descendant(nodeTwo, nodeOne):
        if is_descendant(nodeThree, nodeTwo):
            return True

    return False


def is_descendant_it(node_a, node_b):
    # Check if node_b is descendant of node_a
    current_node = node_a
    while current_node is not None:
        if node_b.value < current_node.value:
            current_node = current_node.left
        elif node_b.value > current_node.value:
            current_node = current_node.right
        else:
            break
    return current_node == node_b


def validateThreeNodes_it(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    # Time O(d)
    # Space O(1)
    if is_descendant(nodeTwo, nodeThree):
        if is_descendant(nodeOne, nodeTwo):
            return True
    elif is_descendant(nodeTwo, nodeOne):
        if is_descendant(nodeThree, nodeTwo):
            return True

    return False


root = BST(5)
root.left = BST(2)
root.right = BST(7)
root.left.left = BST(1)
root.left.right = BST(4)
root.right.left = BST(6)
root.right.right = BST(8)
root.left.left.left = BST(0)
root.left.right.left = BST(3)

nodeOne = root
nodeTwo = root.left
nodeThree = root.left.right.left
print(validateThreeNodes(nodeOne, nodeTwo, nodeThree))
print(validateThreeNodes_it(nodeOne, nodeTwo, nodeThree))
