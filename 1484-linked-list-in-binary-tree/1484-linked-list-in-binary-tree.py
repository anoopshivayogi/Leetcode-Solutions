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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Solution 0 - Brute force
        # Time - O(m * n)
        # Space - O(m + n) - height in case of skewed tree

        if self.helper(head, root):
            return True

        if not root:
            return False

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


    def helper(self, head, root):
        if not head:
            return True

        if not root or root.val != head.val:
            return False

        return self.helper(head.next, root.left) or self.helper(head.next, root.right)

        

