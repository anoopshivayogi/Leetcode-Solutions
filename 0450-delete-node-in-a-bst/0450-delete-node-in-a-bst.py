# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # Solution 1 - Using BST property
        # Time - 
        # Space - 


        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            else:
                cur = root.right # Get the right subtree
                while cur.left:  # Pick the smallest from the right subtree
                    cur = cur.left
                root.val = cur.val  # Replace the value directly
                root.right = self.deleteNode(root.right, cur.val)
        
        return root

                