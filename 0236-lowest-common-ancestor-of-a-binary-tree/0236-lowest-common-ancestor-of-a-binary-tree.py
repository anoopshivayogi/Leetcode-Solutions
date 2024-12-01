# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Solution 1 - using recursive approach 
        # Time - O(N) 
        # Space - O(N) ; if the tree is skewed; worst case will be O(N)


        # res = TreeNode(-1)

        # def dfs(root):
        #     nonlocal res 

        #     if not root:
        #         return False

        #     count = 0

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     if left:
        #         count += 1
        #     if right:
        #         count += 1

        #     mid = (root.val == p.val) or (root.val == q.val)
        #     if mid:
        #         count += 1

        #     if count >= 2:
        #         res = root

        #     return left or right or mid


        # dfs(root)
        # return res


        # if not root:
        #     return False

        # if root and root.val == p.val or root.val == q.val: # if you see a match then that is it 
        #     return root

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right:  # if you see an intersection then that will be your answer overriding the previous one
        #     return root
        # else:
        #     return left or right # Understand that 5 or 0 = 5



        # Re-do for the interview

        # Solution 1
        # Time - O(n)
        # Space - O(n)


        # def dfs(root):
        #     if not root:
        #         return 0

        #     if p.val == root.val or q.val == root.val:
        #         return root

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     if left and right:
        #         return root
        #     else:
        #         return left or right

        # return dfs(root)



        def dfs(node):

            if not node:
                return None

            if node.val == p.val or node.val == q.val:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            else:
                return left or right

        return dfs(root)
            
