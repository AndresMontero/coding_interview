# This is the class of the input root. Do not edit it.
class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def nodeDepths(root, depth=0):
    # Write your code here.
    # Time O(n)
    # Space O(h) where h is the height of the binary tree
    if root is None:
        return 0

    else:
        return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


if __name__ == '__main__':
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
    depth = nodeDepths(tree)
    print(depth)
