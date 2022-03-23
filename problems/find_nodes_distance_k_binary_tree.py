# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def parents_nodes(node, parents_dict, parent=None):
    # Dict to keep track of parents in the binary tree
    if node is not None:
        parents_dict[node.value] = [parent, False]  # to check if already visited in the search ancestors
        parents_nodes(node.left, parents_dict, node)
        parents_nodes(node.right, parents_dict, node)


def find_node_r(node, target, ans):
    # To find specific node
    if node.value == target:
        ans.append(node)
        return True

    if node.left is not None:
        find_node_r(node.left, target, ans)

    if node.right is not None:
        find_node_r(node.right, target, ans)


def search_k_distance_descendants(node, k, curr_distance, neighbors):
    # To find descendants at specific distance
    if node is None or curr_distance > k:
        return

    if node is not None and curr_distance == k:
        neighbors.append(node.value)

    if node.left is not None:
        search_k_distance_descendants(node.left, k, curr_distance + 1, neighbors)

    if node.right is not None:
        search_k_distance_descendants(node.right, k, curr_distance + 1, neighbors)


def search_k_distance_parents(parents_dict, target, k, curr_distance, neighbors):
    # To find ancestors at specific distance
    node = parents_dict[target.value][0]
    if node is None or curr_distance > k:
        return

    parents_dict[node.value][1] = True  # To avoid doing deep search first down again

    if node is not None and curr_distance == k:
        neighbors.append(node.value)

    if node.left is not None and not parents_dict[node.left.value][1]:
        search_k_distance_descendants(node.left, k, curr_distance + 1, neighbors)

    if node.right is not None and not parents_dict[node.right.value][1]:
        search_k_distance_descendants(node.right, k, curr_distance + 1, neighbors)

    search_k_distance_parents(parents_dict, node, k, curr_distance + 1, neighbors)


def findNodesDistanceK(tree, target, k):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    parents_dict = {}
    target_node = []
    neighbors = []

    parents_nodes(tree, parents_dict, None)
    find_node_r(tree, target, target_node)
    target_node = target_node[0]
    search_k_distance_descendants(target_node, k, 0, neighbors)
    parents_dict[target_node.value][1] = True
    search_k_distance_parents(parents_dict, target_node, k, 1, neighbors)
    print(neighbors)

    return neighbors


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.right = BinaryTree(6)
root.right.right.left = BinaryTree(7)
root.right.right.right = BinaryTree(8)
target = 3
k = 2
expected = [2, 7, 8]
print(findNodesDistanceK(root, target, k))
