# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        # Solution 1 - Using DFS and variables
        # Time - O(H) = O(logn) both are same = height of the tree
        # Space - O(H)

        # res = 0
        # closest_diff = float('inf')

        # def dfs(root):
        #     nonlocal closest_diff
        #     nonlocal res

        #     if not root:
        #         return

        #     cur_diff = abs(root.val - target)

        #     if cur_diff <= closest_diff:
        #         if closest_diff == cur_diff:
        #             res = min(root.val, res)
        #         else:
        #             res = root.val
        #             closest_diff = cur_diff

        #     if root.val <= target:
        #         dfs(root.right)
        #     else:
        #         dfs(root.left)

        # dfs(root)

        # return res


        # Solution 2 - Without using recursion - space optimised 
        # Time - O(H) = O(logn) minimum or O(N) maximum
        # Space - O(1)
    
        closest = float('inf')
        res = 0

        while root:
            cur_diff = abs(root.val - target)

            if cur_diff <= closest:

                if cur_diff == closest:
                    res = min(res, root.val)  # If there are multiple answers; print the smallest.
                else:
                    res = root.val
                    closest = cur_diff

            if root.val <= target:
                root = root.right
            else:
                root = root.left

        return res
