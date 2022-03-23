class BinaryTree:
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


def mps(tree):
    if tree is None:
        return (0, float('-inf'))

    left_sum_branch, left_sum_total = mps(tree.left)
    right_sum_branch, right_sum_total = mps(tree.right)
    max_sum_child_branch = max(left_sum_branch, right_sum_branch)

    max_sum_branch = max(tree.value, max_sum_child_branch + tree.value)
    max_sum_total = max(max_sum_branch, left_sum_branch + tree.value + right_sum_branch)
    running_max_path_sum = max(left_sum_total, right_sum_total, max_sum_total)

    return (max_sum_branch, running_max_path_sum)


def maxPathSum(tree):
    # Write your code here.
    # Time O(n)
    # Space O(d)
    print(mps(tree))

    return mps(tree)[1]


test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
print(maxPathSum(test))
