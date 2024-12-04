# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:


        # Solution 1 - Using dfs and prefix sum equals a target SUM problem
        # https://www.youtube.com/watch?v=fFVZt-6sgyo
        # https://leetcode.com/problems/subarray-sum-equals-k/ 
        # Time - O(N)
        # Space - O(N)

        # from collections import defaultdict

        # res = 0
        # prefixes = defaultdict(int)
        # prefixes[0] = 1

        # def dfs(root, total):
        #     nonlocal res
        #     if not root:
        #         return

        #     total += root.val

        #     if total - targetSum in prefixes:
        #         res += prefixes[total - targetSum]

        #     prefixes[total] += 1

        #     dfs(root.left, total)
        #     dfs(root.right, total)

        #     prefixes[total] -= 1  # NOTE: THIS IS VERY VERY IMPORTANT

        # dfs(root, 0)

        # return res


        # Re-do for the interview
        # Time - O(n)
        # Space - O(n)
        
        prefixes = collections.defaultdict(int)
        prefixes[0] = 1
        res = 0

        def dfs(node, total):
            nonlocal res
            if not node:
                return None

            total += node.val

            if total - targetSum in prefixes:
                res += prefixes[total - targetSum]

            prefixes[total] += 1

            dfs(node.left, total)
            dfs(node.right, total)

            prefixes[total] -= 1

        dfs(root, 0)

        return res

        # NOTE: Similar problem : 


        # 1. https://leetcode.com/problems/continuous-subarray-sum/
        # 2. https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
        # 3. https://leetcode.com/problems/path-sum-iii/
        # 4. https://leetcode.com/problems/subarray-sum-equals-k