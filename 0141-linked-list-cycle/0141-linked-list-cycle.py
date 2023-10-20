# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            if slow == fast:
                return True
        return False

# Time complexity - O(n)
# Space complexity - O(1)

# # Hashset solution: 
#         hashset = set()

#         curr = head
#         while curr:
#             hashset.add(curr)
#             curr = curr.next
#             if curr in hashset:
#                 return True
#         return False
        
# # Time Complexity - O(n)
# # Space Complexity - O(n)
        
