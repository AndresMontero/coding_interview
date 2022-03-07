def findClosestValueInBst(tree, target, diff=100000, closest_val=None):
    # Write your code here.
    # Time O(log(n)) on average, worst case O(n)
    # Space O(log(n) on average, worst case O(n)
    if tree.value == target:
        return tree.value
    if abs(target - tree.value) < diff:
        closest_val = tree.value
        diff = abs(target - tree.value)
    if target < tree.value and tree.left is not None:
        closest_val = findClosestValueInBst(tree.left, target, diff, closest_val)
    if target > tree.value and tree.right is not None:
        closest_val = findClosestValueInBst(tree.right, target, diff, closest_val)

    return closest_val


def findClosestValueInBst_it(tree, target, diff=100000, closest_val=None):
    # Write your code here.
    # Time O(log(n)) on average, worst case O(n)
    # Space O(1) on average
    current_node = tree
    while current_node is not None:
        if current_node.value == target:
            return current_node.value
        if abs(target - current_node.value) < diff:
            closest_val = current_node.value
            diff = abs(target - current_node.value)
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break

    return closest_val


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == '__main__':
    coins = [5, 7, 1, 1, 2, 3, 22]

    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    closest_val = findClosestValueInBst(root, 12)
    print(closest_val)

    closest_val = findClosestValueInBst_it(root, 12)
    print(closest_val)
