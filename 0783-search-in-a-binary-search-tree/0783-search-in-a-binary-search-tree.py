# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # Solution 1 - Using recursion
        # Time - O(n)
        # Space - O(n)
        
        # if not root:
        #     return None

        # res = None
        
        # if root.val == val:
        #     res = root
        # elif root.val > val:
        #     res = res or self.searchBST(root.left, val)
        # else:
        #     res = res or self.searchBST(root.right, val)

        # return res


        # Solution 2 - Using iteration
        # Time - 
        # Space - 

        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
            
        return None