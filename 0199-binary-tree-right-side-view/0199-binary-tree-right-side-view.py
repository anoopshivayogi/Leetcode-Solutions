# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # res = []
        # if not root:
        #     return res

        # from collections import deque

        # q = deque([root])

        # while q:
        #     for i in range(len(q)):
        #         popped = q.popleft()
        #         if popped.right:
        #             q.append(popped.right)
        #         if popped.left:
        #             q.append(popped.left)
        #         if i == 0:
        #             res.append(popped.val)

        # return res


        # Re-do for the interview
        # Time - O(n) - Will traverse through each node atleast once.
        # Space - O(n/2) = O(n) - Complete binary tree where the leaf of the tree will have O(n/2) nodes.

        # res = []

        # if not root:
        #     return []

        # from collections import deque

        # q = deque()
        # q.append(root)

        # while q:
        #     for i in range(len(q)):
        #         cur_node = q.popleft()

        #         if i == 0:
        #             res.append(cur_node.val)

        #         if cur_node.right:
        #             q.append(cur_node.right)

        #         if cur_node.left:
        #             q.append(cur_node.left)

        # return res


        # Re-do again for the interview
        # Time - O(N) - You'll traverse all the nodes of the tree
        # Space - O(N) - If one of the layer contains most of the elements in the tree

        # NOTE: Space complexity -- O(D) to keep the queues, where D is a tree diameter. Let's use the last level to estimate the queue size. This level could contain up to N/2 tree nodes in the case of complete binary tree.

        if not root:  # NOTE: Very important base condition for [Breadth first search methods]
            return []

        q = collections.deque()
        q.append(root)

        res = []

        while q:

            for i in range(len(q)):
                cur_node = q.popleft()

                if i == 0:
                    res.append(cur_node.val)

                if cur_node.right:
                    q.append(cur_node.right)

                if cur_node.left:
                    q.append(cur_node.left)

        return res
