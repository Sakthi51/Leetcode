# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # Merge two halfs by re-ordering
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second # inserting second element in between
            second.next = temp1 # after inserting second element, connecting it to third element
            first, second = temp1, temp2 # updating both elements forward

# Time complexity - O(n)
# Space complexity - O(1)
        