# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    # Time O(n) | Space O(1)
    slow, fast = head, head
    ans = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    while slow:
        if ans == slow:
            return ans
        slow = slow.next
        ans = ans.next
