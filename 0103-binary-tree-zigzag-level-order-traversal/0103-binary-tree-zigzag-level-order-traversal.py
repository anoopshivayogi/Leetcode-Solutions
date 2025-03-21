# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Solution 1 - using BFS
        # Time - O(N)
        # Space - O(N)


        if not root:
            return []

        q = collections.deque()
        q.append(root)
        reverse_flag = False

        res = []

        while q:
            cur = []

            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if reverse_flag:
                cur.reverse()

            reverse_flag = not reverse_flag
            res.append(cur)

        return res
