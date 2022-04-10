# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Time O(n)

        # first find the first and second half of the linkedlist
        slow = head
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second list
        second_list = None
        curr = slow.next
        slow.next = None  # break link between first and second list
        while curr:
            tmp = curr.next
            curr.next = second_list
            second_list = curr
            curr = tmp

        # combine two halfs
        first_list = head
        while first_list and second_list:
            next_1 = first_list.next
            next_2 = second_list.next  # save current pointers

            first_list.next = second_list  # update links in middle
            second_list.next = next_1

            first_list = next_1  # update next pointers to continue
            second_list = next_2
