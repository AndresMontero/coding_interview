# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    remainder = 0
    to_divide = 10
    node_1 = linkedListOne
    node_2 = linkedListTwo

    new_head = LinkedList(0)
    current_node = new_head

    while node_1 is not None and node_2 is not None:
        sum_values = node_1.value + node_2.value + remainder
        value_to_add = sum_values % to_divide
        remainder = sum_values // to_divide
        new_node = LinkedList(value_to_add)
        current_node.next = new_node
        current_node = new_node
        node_1 = node_1.next
        node_2 = node_2.next

    while node_1 is not None:
        sum_values = node_1.value + remainder
        value_to_add = sum_values % to_divide
        remainder = sum_values // to_divide
        new_node = LinkedList(value_to_add)
        current_node.next = new_node
        current_node = new_node
        node_1 = node_1.next
    while node_2 is not None:
        sum_values = node_2.value + remainder
        value_to_add = sum_values % to_divide
        remainder = sum_values // to_divide
        new_node = LinkedList(value_to_add)
        current_node.next = new_node
        current_node = new_node
        node_2 = node_2.next

    if remainder > 0:
        new_node = LinkedList(remainder)
        current_node.next = new_node
        current_node = new_node

    return new_head.next


def sumOfLinkedLists_2(linkedListOne, linkedListTwo):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    remainder = 0
    to_divide = 10
    node_1 = linkedListOne
    node_2 = linkedListTwo

    new_head = LinkedList(0)
    current_node = new_head

    while node_1 is not None or node_2 is not None or remainder > 0:
        value_1 = node_1.value if node_1 is not None else 0
        value_2 = node_2.value if node_2 is not None else 0
        sum_values = value_1 + value_2 + remainder

        value_to_add = sum_values % to_divide
        remainder = sum_values // to_divide
        new_node = LinkedList(value_to_add)
        current_node.next = new_node
        current_node = new_node

        node_1 = node_1.next if node_1 is not None else None
        node_2 = node_2.next if node_2 is not None else None

    return new_head.next
