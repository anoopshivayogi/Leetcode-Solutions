# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        # def dfs(p, q):

        #     if not p and not q:
        #         return True
            
        #     if not p or not q:
        #         return False

        #     left, right = dfs(p.left, q.left), dfs(p.right, q.right)

        #     if not left or not right or p.val != q.val:
        #         return False

        #     return True
        
        # return dfs(p, q)




        # def dfs(left, right):

        #     if not left and not right:
        #         return True

        #     if not left or not right:
        #         return False


        #     if left.val != right.val:
        #         return False


        #     if not dfs(left.left, right.left) or not dfs(left.right, right.right):
        #         return False


        #     return True

        # return dfs(p, q)








        # def dfs(p, q):
        #     if not p and not q:
        #         return True 

        #     if not p or not q:
        #         return False 

        #     if p.val != q.val:
        #         return False


        #     if not dfs(p.left, q.left) or not dfs(p.right, q.right):
        #         return False

        #     return True


        # return dfs(p, q)




        # Re-do for the interview
        # Time - O(n) ; all nodes atleast once
        # Space - O(n) ; skwewed tree


        def dfs(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            if dfs(p.left, q.left) and dfs(p.right, q.right):
                return True

            return False

        return dfs(p, q)
