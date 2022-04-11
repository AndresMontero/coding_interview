"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# def clone(node, mapping):
#     if node in mapping:
#         return mapping[node]

#     tmp_copy = Node(node.val)
#     mapping[node] = tmp_copy

#     for neig in node.neighbors:
#         tmp_copy.neighbors.append(clone(neig, mapping))

#     return tmp_copy
# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         # Time O(n + e) where n is the number of nodes and e the number of edges
#         # Space O(n)
#         if node is None:
#             return None

#         mapping = {}

#         return clone(node, mapping)

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Time O(n + e) | Space O(n)
        if not node:
            return None

        nodes_visited = {}
        new_root = Node(node.val)
        nodes_visited[node] = new_root

        stack = [node]

        while stack:
            curr_node = stack.pop()
            for neigh in curr_node.neighbors:
                if neigh not in nodes_visited:
                    stack.append(neigh)
                    nodes_visited[neigh] = Node(neigh.val)

                nodes_visited[curr_node].neighbors.append(nodes_visited[neigh])

        return nodes_visited[node]



