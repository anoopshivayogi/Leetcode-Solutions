# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Solution 1 - straightup DFS
        # Time - O(n)
        # Space - O(logn)

        # if not root:
        #     return None

        # def recursive(root):

        #     res = 0

        #     if not root:
        #         return res

        #     if low <= root.val <= high:
        #         res += root.val

        #     res += recursive(root.left)
        #     res += recursive(root.right)

        #     return res

        # return recursive(root)


        # Solution 2 - Trying to use BST properties
        # Time - O(logn) = O(n) cz for not balanced tree
        # Space - O(logn) 


        # def recursive(root):

        #     res = 0

        #     if not root:
        #         return res

        #     if low <= root.val <= high:
        #         res += root.val
        #         res += recursive(root.left)
        #         res += recursive(root.right)
        #     else:
        #         if root.val < low:
        #             res += recursive(root.right)
        #         elif root.val > high:
        #             res += recursive(root.left)

        #     return res

        # return recursive(root)



        # Re-do for the interview 

        # def dfs(root):

        #     if not root:
        #         return 0

        #     res = 0

        #     if low <= root.val <= high:
        #         res += root.val

        #         res += dfs(root.left)
        #         res += dfs(root.right)

        #     return res

        # return dfs(root)




        # Re-do for the interview
        # Time - O(n)
        # Space - O(n) or height of the tree


        # res = 0

        # def dfs(root):
        #     nonlocal res
        #     if not root:
        #         return 0


        #     if low <= root.val <= high:
        #         res += root.val

        #     dfs(root.left)
        #     dfs(root.right)

        #     return res


        # return dfs(root)


        # Re-do for the interview - Using BST properties
        # Time - 
        # Space - 


        # def dfs(node):

        #     if not node:
        #         return

        #     if low <= node.val <= high:
        #         self.res += node.val
        #         dfs(node.left)
        #         dfs(node.right)
        #     else:
        #         if node.val <= low:
        #             dfs(node.right)
        #         elif node.val >= high:
        #             dfs(node.left)

        # dfs(root)
        # return self.res


        def dfs(node):

            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)

            elif node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)


        
