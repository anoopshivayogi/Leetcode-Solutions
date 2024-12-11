class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:


        # Intuition

        # 3 : [0, 1], 6: [3]

        # Solution 1 -
        # Time - nlogn
        # Space - O(n)

        res = [set() for _ in range(n)]

        adj_lst = collections.defaultdict(list)
        in_degree = [0] * n

        for e1, e2 in edges:
            adj_lst[e1].append(e2)
            in_degree[e2] += 1

        q = collections.deque()

        for node in range(n):
            if in_degree[node] == 0:
                q.append(node)

        while q:
            popped = q.popleft()

            for neigh in adj_lst[popped]:
                res[neigh].update(res[popped])
                res[neigh].add(popped)

                in_degree[neigh] -= 1

                if in_degree[neigh] == 0:
                    q.append(neigh)

        res = [sorted(list(item)) for item in res]

        return res
