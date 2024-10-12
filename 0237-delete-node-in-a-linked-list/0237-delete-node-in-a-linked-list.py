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

        # Solution 1 - 
        # Time - 
        # Space -

        while node.next.next:
            node.val = node.next.val
            node = node.next

        node.val = node.next.val
        node.next = node.next.next


        # Solution 2 - Constant solution by overwriting
        # Time - O(1)
        # Space - O(1)
        
        # node.val = node.next.val
        # node.next = node.next.next