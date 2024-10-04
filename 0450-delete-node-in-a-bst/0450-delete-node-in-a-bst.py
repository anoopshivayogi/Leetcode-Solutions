# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # Solution 1 - Using BST property
        # https://www.youtube.com/watch?v=LFzAoJJt92M
        # Time - O(logn + logn) = O(logn) or height of the tree; worst case in skewed tree it can be O(n)
        # Space - O(logn) or height of the tree


        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:

            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                cur = root.right # Get the right subtree
                while cur.left:  # Pick the smallest from the right subtree
                    cur = cur.left
                root.val = cur.val  # Replace the value directly
                root.right = self.deleteNode(root.right, cur.val)
        
        return root


        # Dry - run

        # root = [5,3,6,2,4,null,7], key = 3

        #           5
        #      4          6
        #  2     4    nul    7
                

        # stack = [deleteNode(3, 3), deleteNode(4, 4)]
        # root = 4
