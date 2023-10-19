# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node and make it as head
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # move right pointer to the desired place
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # increment both right and left until right is out of bounce
        while right:
            left = left.next
            right = right.next

        # delete the value in the left pointer
        left.next = left.next.next
        # leave dummy node and return from the first node
        return dummy.next

        