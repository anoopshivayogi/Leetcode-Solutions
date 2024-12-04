# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # def dfs(root):
        #     maxLeft = 0
        #     maxRight = 0

        #     if root.left:
        #         maxLeft = 1 + dfs(root.left)
        #     if root.right:
        #         maxRight = 1 + dfs(root.right)

        #     self.res = max(self.res, maxLeft + maxRight)

        #     return max(maxLeft, maxRight)

        # dfs(root)

        # return self.res


        # res = 0

        # def dfs(root):
        #     nonlocal res

        #     if not root:
        #         return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     res = max(res, left + right)

        #     return 1 + max(left, right)

        # dfs(root)
        # return res


        # if not root:
        #     return 0

        # res = 0

        # def dfs(root):
        #     nonlocal res

        #     if not root:
        #         return 0

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     res = max(res, left+right)

        #     return 1 + max(left, right)

        # dfs(root)

        # return res



        # res = [0]

        # def dfs(root):

        #     if not root:
        #         return 0


        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     res[0] = max(res[0], left + right)

        #     return 1 + max(left, right)


        # dfs(root)

        # return res[0]


        # Re-do for the interview
        # Time - O(n)
        # Space - O()

        # res = [0]

        # def dfs(root):
        #     if not root:
        #         return 0

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     res[0] = max(res[0], left + right)
        #     return 1 + max(left, right)

        # dfs(root)

        # return res[0]


        # Re-do for the interview 
        # Time - O(n)
        # Space - O(logn) in beest case and O(n) - In case of skewed worst case

        # res = 0

        # def dfs(node):
        #     nonlocal res

        #     if not node:
        #         return 0

        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     res = max(res, left + right)

        #     return 1 + max(left, right)

        # dfs(root)

        # return res


        # Follow-up: print the path of the diameter?
        # Time - 
        # Space - 


        res = 0
        res_path = []

        def dfs(node):
            nonlocal res, res_path

            if not node:
                return 0, []

            left, left_path = dfs(node.left)
            right, right_path = dfs(node.right)

            if left + right > res:
                res = left + right
                res_path = left_path + [node.val] + right_path

            if left > right:
                return (1 + left, left_path + [node.val])
            else:
                return (1 + right, right_path + [node.val])

        dfs(root)
        print(res_path)
        return res

        # NOTE: Follow up hard question - https://leetcode.com/problems/binary-tree-maximum-path-sum/


        # Tracing

        # [dfs(1), dfs(2), dfs(5)]
        # left return - 1
        # right return - 1
        # function return - 2
        # res = 2
