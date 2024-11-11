# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Solution 1 - 
        # Time - 
        # Space - 

        nodes_found = False

        def dfs(node):
            nonlocal nodes_found

            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            conditions = 0

            if node.val == p.val or node.val == q.val:
                conditions += 1
            
            if left:
                conditions += 1

            if right:
                conditions += 1

            if conditions >= 2:
                nodes_found = True

            if (node.val == p.val or node.val == q.val) or (left and right):
                return node

            return left or right

        ans = dfs(root)

        return ans if nodes_found else None
