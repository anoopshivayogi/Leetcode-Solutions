class Solution:
    def canFinish(self, crs: int, pre: List[List[int]]) -> bool:


        # adjMap = collections.defaultdict(list)
        # visit = set()

        # for crs in prerequisites:
        #     adjMap[crs[0]].append(crs[1])


        # def dfs(crs):

        #     if not adjMap[crs]:
        #         return True

        #     if crs in visit:
        #         return False

        #     visit.add(crs)

        #     for each_crs in adjMap[crs]:
        #         if not dfs(each_crs):
        #             return False

        #     visit.remove(crs)
        #     adjMap[crs] = []

        #     return True


        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False

        # return True



        # adjM = {}
        # visit = set()

        # for p in pre:
        #     if p[0] in adjM:
        #         adjM[p[0]].append(p[1])
        #     else:
        #         adjM[p[0]] = [p[1]]


        # def dfs(node):
        #     if node in visit:
        #         return False

        #     visit.add(node)

        #     if node in adjM:
        #         for n in adjM[node]:
        #             if not dfs(n):
        #                 return False

        #     visit.remove(node)
        #     # adjM[node] = []

        #     return True


        # for c in range(crs-1):
        #     if not dfs(c):
        #         return False

        # return True


        # Solution 1 - DFS with visit -- visit only for that particular path 
        # Time - O(E + V) 
        # Space - O(E + V)

        # adjM = { i: [] for i in range(crs) }

        # for p in pre:
        #     adjM[p[1]].append(p[0])

        # visit = set()

        # def dfs(node):
        #     if node in visit:
        #         return False

        #     visit.add(node)

        #     for n in adjM[node]:
        #         if not dfs(n):
        #             return False

        #     visit.remove(node)
        #     adjM[node] = []

        #     return True

        # for each_crs in range(crs):
        #     if not dfs(each_crs):
        #         return False

        # return True


        # Solution 2 - Khan's algorithm - Topological sorting
        # Time - O(m + n) ; where m = edges and n = indegree
        # Space - O(m + n) ; same as above. You can also say O(E + V) its the same

        # from collections import deque

        # inDegree = [0] * crs
        # q = deque()
        # res = []

        # adjM = {i:[] for i in range(crs)}

        # for p in pre:
        #     adjM[p[1]].append(p[0])
        #     inDegree[p[0]] += 1

        # # Push all the nodes with indegree == 0

        # for i in range(crs):
        #     if inDegree[i] == 0:
        #         q.append(i)

        # count = 0

        # while q:
        #     p = q.popleft()

        #     for n in adjM[p]:
        #         print(n)
        #         inDegree[n] -= 1
        #         if inDegree[n] == 0:
        #             q.append(n)

        #     res.append(p)
        #     count += 1

        # if len(res) != crs:
        #     return False

        # return True


        # Re-do for the interview
        # Time - O(V+E)
        # Space - O(V+E)

        # q = collections.deque()
        # adj_list = defaultdict(list)
        # in_degree = [0] * crs

        # for p in pre:     # NOTE: O(E) SAME FOR SPACE
        #     adj_list[p[1]].append(p[0])   
        #     in_degree[p[0]] += 1

        # for i in range(crs):      # NOTE: O(V) SAME FOR SPACE 
        #     if in_degree[i] == 0:
        #         q.append(i)

        # while q:
        #     popped_node = q.popleft()
        #     crs -= 1

        #     for neigh in adj_list[popped_node]:
        #         in_degree[neigh] -= 1
        #         if in_degree[neigh] == 0:
        #             q.append(neigh)

        # if crs == 0:
        #     return True

        # return False



        # Lets try Union-Find
        # Union Find will be very difficult in this problem

        # class UnionFind:
        #     def __init__(self, n):
        #         self.n = n
        #         self.rank = [1] * n
        #         self.parents = [i for i in range(self.n)]

        #     def find(self, node):
        #         while node != self.parents[node]:
        #             self.parents[node] = self.parents[self.parents[node]] # Path compression
        #             node = self.parents[node]

        #         return node

        #     def union(self, n1, n2):
        #         node1 = self.find(n1)
        #         node2 = self.find(n2) 

        #         if node1 == node2:
        #             return True 

        #         if self.rank[node1] >= self.rank[node2]:
        #             self.parents[node2] = node1 
        #             self.rank[node1] += 1
        #         else:
        #             self.parents[node1] = node2
        #             self.rank[node2] += 1

        #         return False

        # uf_obj = UnionFind(crs)
        # count = 0

        # for p in pre:
        #     count += 1
        #     if uf_obj.union(p[0], p[1]):
        #         return False

        # return count == (crs - 1)
              

        adj_mat = collections.defaultdict(list)
        in_degree = [0] * crs

        for p0, p1 in pre:
            adj_mat[p1].append(p0)
            in_degree[p0] += 1

        q = collections.deque()

        for i in range(crs):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            cur_node = q.popleft()
            crs -= 1

            for neigh in adj_mat[cur_node]:
                in_degree[neigh] -= 1

                if in_degree[neigh] == 0:
                    q.append(neigh)


        if crs == 0:
            return True

        return False


