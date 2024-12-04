# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        # Solution 1 - 
        # Time - 
        # Space - 

        res = root.val

        # Without split
        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left = max(0, left)
            right = max(0, right)
            
            # With split 
            res = max(res, left + right + node.val)

            return node.val + max(left, right)

        dfs(root)

        return res
