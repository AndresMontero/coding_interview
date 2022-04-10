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


def sumOfLinkedLists(l1, l2):
    # Write your code here.
    # Time O(n) | Space O(n) where n is the max(len(l1), len(l2))
    carry = 0
    result = LinkedList(0)
    result_head = result

    while l1 or l2:
        val_1 = l1.value if l1 else 0
        val_2 = l2.value if l2 else 0

        val = (val_1 + val_2 + carry) % 10
        result.next = LinkedList(val)
        carry = (val_1 + val_2 + carry) // 10
        result = result.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry > 0:
        result.next = LinkedList(carry)

    return result_head.next
