class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


linkedListClass = StartLinkedList


class LinkedList(linkedListClass):
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


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    pointer_1 = head
    pointer_2 = head
    for i in range(k):
        pointer_2 = pointer_2.next

    if pointer_2 is None:
        head.value = head.next.value
        head.next = head.next.next
    else:
        while pointer_2.next is not None:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
        pointer_1.next = pointer_1.next.next


if __name__ == "__main__":
    test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(test.getNodesInArray())
    removeKthNodeFromEnd(test, 4)
    print(test.getNodesInArray())
