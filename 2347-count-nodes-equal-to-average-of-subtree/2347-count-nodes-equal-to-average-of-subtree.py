# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def averageOfSubtree(self, root: TreeNode) -> int:
        # Time - O(N)
        # Space - O(N)

        # def dfs(node):
        #     if not node:
        #         return (0, 0)

        #     node_left, total_left = dfs(node.left)
        #     node_right, total_right = dfs(node.right)

        #     subtree_total = (total_left + total_right + node.val)
        #     subtree_nodes = (node_left + node_right + 1)
        #     subtree_avg = (subtree_total // subtree_nodes)

        #     if subtree_avg == node.val:
        #         self.res += 1

        #     return (subtree_nodes, subtree_total)

        # dfs(root)

        # return self.res



        # Re-do for the interview
        # Time - O(n)
        # Space - O(n)

        res = [0]

        def dfs(node):
            if not node:
                return (0, 0)  # number of node, sum

            left_nodes, left_sum = dfs(node.left)
            right_nodes, right_sum = dfs(node.right)

            total_nodes = left_nodes + right_nodes + 1
            total_sum = left_sum + node.val + right_sum

            avg = total_sum // total_nodes

            if avg == node.val:
                res[0] += 1

            return (total_nodes, total_sum)


        dfs(root)

        return res[0]
