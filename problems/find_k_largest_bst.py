# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inOrderTraverse(tree, array=[]):
    if tree is None:
        return

    if tree.left:
        inOrderTraverse(tree.left, array)

    array.append(tree.value)

    if tree.right:
        inOrderTraverse(tree.right, array)

    return array


def findKthLargestValueInBst(tree, k):
    # Time O(n) because we are traversing the entire tree
    # Space O(n) because we are saving the entire numbers
    array = []
    numbers = inOrderTraverse(tree, array)
    print(numbers, k)
    return numbers[-k]


def inReverseOrderTraverse(tree, k, array=[]):
    if tree is None:
        return

    if len(array) >= k:
        return array

    if tree.right:
        inReverseOrderTraverse(tree.right, k, array)

    array.append(tree.value)

    if tree.left:
        inReverseOrderTraverse(tree.left, k, array)

    return array


def findKthLargestValueInBst_2(tree, k):
    # Time O(d + k) where d is the depth of the ree and k is the number of nodes
    # Space O(k)
    array = []
    numbers = inReverseOrderTraverse(tree, k, array)
    print(numbers, numbers[k - 1], k)
    return numbers[k - 1]


if __name__ == '__main__':
    root = BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.left = BST(17)
    root.right.right = BST(22)
    print(findKthLargestValueInBst(root,3))
    print(findKthLargestValueInBst_2(root,3))