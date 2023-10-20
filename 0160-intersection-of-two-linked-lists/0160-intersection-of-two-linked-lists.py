# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Find the length of the two linked lists
        dummy1, dummy2 = ListNode(0, headA), ListNode(0, headB)
        length1, length2 = 0, 0
        while dummy1:
            dummy1 = dummy1.next
            length1 += 1
        while dummy2:
            dummy2 = dummy2.next
            length2 += 1
        print(length1, length2)

        # If any one of the linked list is greater than other move pointer of longest one by the difference
        if length1 > length2:
            while length1 > length2:
                headA = headA.next
                length1 -= 1
        else:
            while length2 > length1:
                headB = headB.next
                length2 -= 1
        
        # Then compare both headA and headB, if they don't intersect return "None"
        while headA and headB:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
        return None
    
# Time complexity - O(n)
# Space complexity - O(1)

        # # Hashset solution
        # first_set = set()
        # curr = headA

        # while curr:
        #     first_set.add(curr)
        #     curr = curr.next

        # curr = headB
        # while curr:
        #     if curr in first_set:
        #         return curr
        #     curr = curr.next
        # return None