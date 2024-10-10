# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # Solution 1 - Using recursion
        # Time - O(n) - O(LogN) or height of the tree in average case and O(N) in worst case - skewed
        # Space - O(n) - same with the space
        
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
        # Time - O(N) - same as previous solution
        # Space - O(1)

        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
            
        return None