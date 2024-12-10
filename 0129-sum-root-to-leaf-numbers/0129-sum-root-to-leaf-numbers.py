# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Solution 1 - Using dfs
        # Time - O(n)
        # Space - O(H)- worst case O(n) in case of skewed tree

        self.res = 0

        self.dfs(root, 0)

        return self.res



    def dfs(self, root, path):

        if not root:
            return

        path = path * 10 + root.val

        if not root.left and not root.right:
            self.res += path
            return

        self.dfs(root.left, path)
        self.dfs(root.right, path)
