"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Time O(n)
        # Space O(n)

        nodes_dict = {None: None}  # Needed None: None for the edge case where next is none
        node = head
        while node:  # First pass to simply create nodes with value and store them in a hash table
            nodes_dict[node] = Node(node.val, None, None)
            node = node.next

        node = head
        while node:  # Second pass to connect pointers
            new_node = nodes_dict[node]
            new_node.next = nodes_dict[node.next]
            new_node.random = nodes_dict[node.random]
            node = node.next

        return nodes_dict[head]  # Return the new head that is stored in the hash map
