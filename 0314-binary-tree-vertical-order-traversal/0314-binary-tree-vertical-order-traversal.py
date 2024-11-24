# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Solution 0 - using DFS
        # Complicated solution for DFS since we need from top to bottom wise values
        # Normal DFS would not do top to bottom hence the issue.
        # Solution is to group by col_num and then sort it by row_num -> below code has errors.

        # nodes = collections.defaultdict(list)

        # def dfs(node, row, col):
        #     if not node:
        #         return

        #     nodes[col].append((row, node.val))

        #     dfs(node.left, row + 1, col - 1)
        #     dfs(node.right, row + 1, col + 1)

        # dfs(root, 0, 0)

        # res = sorted(nodes.items(), key=lambda item: (item[0], item[1][0]))

        # print(res)
        # # [(-1, [(1, 9)]), (0, [(0, 3), (2, 15)]), (1, [(1, 20)]), (2, [(2, 7)])]

        # res = [[i[1] for i in item[1]] for item in res]

        # return res


        # Solution 1 - using BFS
        # Time - O(N)
        # Space - O(N)


        # NOTE: Important edge condition to handle

        # if not root:
        #     return root

        # q = collections.deque()
        # q.append((root, 0))

        # nodes = collections.defaultdict(list)

        # while q:
        #     node, col = q.popleft()

        #     nodes[col].append(node.val)

        #     if node.left:
        #         q.append((node.left, col - 1))

        #     if node.right:
        #         q.append((node.right, col + 1))

        # res = sorted(nodes.items(), key=lambda item: item[0])

        # res = [item[1] for item in res]

        # return res


        # Solution 3 - By not using sorting; just use two pointer to store max and min cols
        # Time - O(N)
        # Space - O(N)
        
        # NOTE: Take care of the base case when root is None seperately

        # if not root:
        #     return []

        # queue = collections.deque()
        # queue.append((0, root))

        # level_items = collections.defaultdict(list)
        # min_col, max_col = float('inf'), float('-inf')

        # res = []

        # while queue:
        #     col, node = queue.popleft()

        #     min_col = min(min_col, col)
        #     max_col = max(max_col, col)

        #     level_items[col].append(node.val)

        #     if node.left:
        #         queue.append((col - 1, node.left))

        #     if node.right:
        #         queue.append((col + 1, node.right))


        # for i in range(min_col, max_col + 1):
        #     res.append(level_items[i])

        # return res


        # Re-do for the interview
        # Time - 
        # Space - 

        if not root:
            return []

        col_list = collections.defaultdict(list)
        q = collections.deque()
        q.append((root, 0)) # (node, col)
        max_col, min_col = float("-inf"), float("inf")
        res = []

        while q:
            cur_node, col = q.popleft()
            col_list[col].append(cur_node.val)

            max_col, min_col = max(max_col, col), min(min_col, col)

            if cur_node.left:
                q.append((cur_node.left, col - 1))

            if cur_node.right:
                q.append((cur_node.right, col + 1))


        for col in range(min_col, max_col + 1):
            res.append(col_list[col])

        return res