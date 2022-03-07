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


def calculate_branch_sum(node, branch_sum, branch_sums):
    branch_sum += node.value

    if node.left is None and node.right is None:
        branch_sums.append(branch_sum)
        return

    if node.left is not None:
        calculate_branch_sum(node.left, branch_sum, branch_sums)
    if node.right is not None:
        calculate_branch_sum(node.right, branch_sum, branch_sums)


def branchSums(root, branch_sum=0, branch_sums=[]):
    # Write your code here.
    # Time O(n)
    # Space O(n) -> due to the recursion
    branch_sums = []
    calculate_branch_sum(root, 0, branch_sums)

    return branch_sums


if __name__ == '__main__':
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
    branch_sums = branchSums(tree)
    print(branch_sums)
