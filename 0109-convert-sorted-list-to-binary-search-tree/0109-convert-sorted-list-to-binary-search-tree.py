# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        # Solution 1 - Divide and conquer style 
        # Time - O(nlogn) - Not sure how; We compute middle element for half of the linkedlist again and again
        # Space - O(logn) - In this case there is no skewing and no O(n)
        
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)  # NOTE: Mistake made in this place !! be careful

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        second = slow.next  # Get the start of the second part of the linkedList
        prev.next = None # End the first part of the linkedList

        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(second)

        return root