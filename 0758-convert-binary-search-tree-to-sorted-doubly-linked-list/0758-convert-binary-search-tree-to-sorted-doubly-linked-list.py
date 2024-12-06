"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # Solution 1 - In-order traversal with first and last pointer
        # Time - O(N)
        # Space - O(N) if its a skwewed tree; O(LogN) for the best case of completely balanced tree
        # https://www.youtube.com/watch?v=l1hSUOaXLxc

        # if not root:
        #     return None

        # self.first, self.last = None, None
        # self.in_order_link(root)
        # self.first.left, self.last.right = self.last, self.first

        # return self.first


    # def in_order_link(self, root):

    #     if root:
    #         self.in_order_link(root.left)

    #         if not self.first:
    #             self.first = root
    #         else:
    #             self.last.right = root
    #             root.left = self.last

    #         self.last = root

    #         self.in_order_link(root.right)

        # Re-do for the interview
        # Time - O(n)
        # Space - O(logn) or height of the tree in case of balanced or O(n) in skewed worst case

        if not root:
            return None

        self.first, self.last = None, None
        self.in_order_link(root)
        self.first.left = self.last
        self.last.right = self.first

        return self.first


    def in_order_link(self, node):
        
        if node:
            self.in_order_link(node.left)

            if not self.first:
                self.first = node
            else:
                self.last.right = node
                node.left = self.last

            self.last = node

            self.in_order_link(node.right)




    # Re-do for the interview
    # Time - 
    # Space - 


