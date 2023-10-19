# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next # holding the reference for next varible
            curr.next = prev # pointing the current point to previous variable
            prev = curr # incrementing the prev to next
            curr = nxt # incrementing the curr to next
        return prev

# Time complexity - O(n)
# Space complexity - O(1)