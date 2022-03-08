# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self
    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    node = linkedList
    while node is not None:
        next_node = node.next
        while next_node is not None and node.value == next_node.value:
            next_node = next_node.next
        node.next = next_node
        node = next_node

    return linkedList



if __name__ == '__main__':
    test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
    actual = removeDuplicatesFromLinkedList(test)
    print(actual)