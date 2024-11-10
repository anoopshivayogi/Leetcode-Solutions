# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Solution 1 - Using DFS
        # Time - O(n)
        # Space - O(n)


        def dfs(root):

            if not root:
                return None

            left = dfs(root.left)
            right = dfs(root.right)

            if not left:
                root.left = None

            if not right:
                root.right = None

            return root.val or left or right


        dfs(root)

        return root if dfs(root) else None