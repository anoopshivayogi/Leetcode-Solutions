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

        res = 0

        def dfs(root, path):
            nonlocal res
            if not root:
                return

            path += str(root.val)

            dfs(root.left, path)
            dfs(root.right, path)

            if not root.left and not root.right:
                res += int(path)
                return

        dfs(root, '')

        return res
