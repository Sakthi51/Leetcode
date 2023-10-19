# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Here's an example to illustrate this:

        # Suppose you have a linked list like this: 1 -> 2 -> 3 -> 4, and you want to delete node 2.

        # Copy the value of node 3 into node 2: 1 -> 3 -> 3 -> 4.
        # Update the "next" pointer of node 2 to skip over the duplicate node 3: 1 -> 3 -> 4.
        # Now, node 2 effectively holds the value of node 3, and node 3 is removed from the list.
        node.val = node.next.val
        node.next = node.next.next
        
# Regardless of size we do same thing in all problems       
# Time complexity - O(1)
# Space complexity - O(1)