# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:


        # Solution 0 - using BFS -- Level order traversal
        # Time - O(N)
        # Space - O(N)

        # q = collections.deque()
        # q.append(root)

        # while q:
        #     node = q.popleft()

        #     if node:
        #         q.append(node.left)
        #         q.append(node.right)
        #     else:
        #         while q:
        #             node = q.popleft()
        #             if node:
        #                 return False

        # return True



        q = collections.deque([root])

        while q:
            cur_node = q.popleft()

            if cur_node:
                q.append(cur_node.left)
                q.append(cur_node.right)
            else:
                while q:
                    nxt_node = q.popleft()
                    if nxt_node:
                        return False

        return True