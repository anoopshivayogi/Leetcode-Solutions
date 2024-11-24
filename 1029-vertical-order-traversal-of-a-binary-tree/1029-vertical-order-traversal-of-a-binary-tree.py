# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        # Solution 1 - Using BFS
        # Time - O(N) + Nlog(N/k); where k is the max width of the tree -> O(N) + Nlog(N)
        # Space - O(N)

        # https://www.youtube.com/watch?v=_8yW-dQVJHM

        if not root:  # NOTE: check this edge conditon IMP !!
            return []

        level_items = collections.defaultdict(list)
        q = collections.deque()
        q.append((0, 0, root))
        levels = []
        min_level, max_level = float("inf"), float("-inf")

        while q:
            row, col, node = q.popleft()
            level_items[col].append((node.val, row))

            min_level = min(min_level, col)
            max_level = max(max_level, col)

            if node.left:
                q.append((row + 1, col-1, node.left))
            
            if node.right:
                q.append((row + 1, col+1, node.right))

        res = []

        for i in range(min_level, max_level + 1):
            item = level_items[i]
            item.sort(key = lambda x: (x[1], x[0]))  # NOTE: Sort by row and then by value
            item = [x[0] for x in item]
            res.append(item)

        return res
