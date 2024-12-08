# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        # if k == 0:
        #     return [target.val]

        # from collections import defaultdict, deque

        # adjM = defaultdict(list)

        # q = deque()
        # q.append(root)

        # while q:
        #     popped = q.pop()

        #     if popped.left:
        #         adjM[popped].append(popped.left)
        #         adjM[popped.left].append(popped)

        #         q.append(popped.left)

        #     if popped.right:
        #         adjM[popped].append(popped.right)
        #         adjM[popped.right].append(popped)

        #         q.append(popped.right)


        # # BFS shortest path from the target node 

        # res = []
        # visit = set()

        # q = deque()
        # q.append(target)
        # visit.add(target)

        # while q and k > 0:

        #     for _ in range(len(q)):
        #         popped = q.popleft()

        #         for neigh in adjM[popped]:
        #             if neigh not in visit:
        #                 visit.add(neigh)
        #                 q.append(neigh)

        #     k -= 1

        # while q:
        #     res.append(q.popleft().val)

        # return res



        # Re - Do 
        # Time - 
        # Space - 

        res = []
        adj_list = collections.defaultdict(list)

        def dfs(node):
            if node.left:
                adj_list[node].append(node.left)
                adj_list[node.left].append(node)
                dfs(node.left)

            if node.right:
                adj_list[node].append(node.right)
                adj_list[node.right].append(node)
                dfs(node.right)

        dfs(root)

        q = collections.deque()
        q.append((target, 0))
        visit = set()
        visit.add(target)

        while q:
            node, i = q.popleft()

            if i == k:
                res.append(node.val)

            if i + 1 <= k:
                for neigh in adj_list[node]:
                    if neigh not in visit:
                        q.append((neigh, i + 1))
                        visit.add(neigh)

        return res
