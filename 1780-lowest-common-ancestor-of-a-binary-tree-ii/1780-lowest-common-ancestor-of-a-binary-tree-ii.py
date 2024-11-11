# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Solution 1 - DFS solution ; modified version of the primary LCA question
        # Time - O(n)
        # Space - O(h) = O(n) in worst case for a skwed tree the height will be equal to the number of nodes

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

        ans = dfs(root)  # NOTE: Apparently this is very important; You cannot directly return dfs() if <condition>

        return ans if nodes_found else None


        # In the code for finding the lowest common ancestor (LCA) of two nodes in a binary tree, there’s a subtle reason why directly returning dfs(root) if nodes_found else None does not work as intended.

# The issue lies in the evaluation of nodes_found in return dfs(root) if nodes_found else None. When this line is executed, nodes_found may not yet be True, even if the DFS (depth-first search) function dfs has identified the LCA. This is because dfs only marks nodes_found = True during the recursive exploration when the LCA node is identified. However, nodes_found may still be False at the time dfs(root) finishes, depending on the traversal order and whether the function was able to set nodes_found early in the traversal.
