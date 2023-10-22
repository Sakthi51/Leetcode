# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # create a dummy node and make first element as head
        dummy = ListNode(next = head)
        prev, curr = dummy, head

        while curr:
            nxt = curr.next

            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            
            curr = nxt
        return dummy.next

# Time complexity - O(n)
# Space complexity - O(1)