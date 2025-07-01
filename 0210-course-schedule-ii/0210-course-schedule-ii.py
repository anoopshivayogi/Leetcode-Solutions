class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
#         # courses = {x: [] for x in range(numCourses)}
#         # seen, cycle = set(), set()
#         # output = []

#         # for p in prerequisites:
#         #     courses[p[0]].append(p[1])

#         # def dfs(crs):

#         #     if crs in seen:
#         #         return True
            
#         #     if crs in cycle:
#         #         return False

#         #     cycle.add(crs)

#         #     for c in courses[crs]:
#         #         if not dfs(c):
#         #             return False
                
#         #     cycle.remove(crs)      
#         #     seen.add(crs)

#         #     output.append(crs)

#         #     return True


#         # for crs in range(numCourses):
#         #     if not dfs(crs):
#         #         return []

#         # return output


#         # Solution 2 - Khan's algorithm
#         # Time - O(E + V)
#         # Space - O(E + V) space for indegree -- stores nodes and edges -- stored in adjM

#         # res = []
#         # adjL = defaultdict(list)
#         # indegrees = defaultdict(int)
        
#         # for p in prerequisites:
#         #     adjL[p[1]].append(p[0])
#         #     indegrees[p[0]] += 1
        
#         # q = deque()
            
#         # for i in range(numCourses):
#         #     if i not in indegrees:
#         #         q.append(i)

        
#         # while q:
#         #     p = q.popleft()
#         #     res.append(p)
            
#         #     for neigh in adjL[p]:
#         #         indegrees[neigh] -= 1
#         #         if indegrees[neigh] == 0:
#         #             q.append(neigh)
        
        
#         # return res if len(res) == numCourses else []


#         # Solution - Khan's algorithm
#         # Time - O(E + V)
#         # Space - O(E + V)

#         # from collections import deque

#         # adjM = {i:[] for i in range(numCourses)}
#         # inDegree = [0] * numCourses

#         # for p in prerequisites:
#         #     adjM[p[1]].append(p[0])
#         #     inDegree[p[0]] += 1

#         # # push all the nodes with in-degree == 0

#         # q = deque()

#         # for i in range(numCourses):
#         #     if inDegree[i] == 0:
#         #         q.append(i)

#         # res = []

#         # while q:
#         #     for i in range(len(q)):
#         #         p = q.popleft() # Both DFS and BFS works equally well for this one

#         #         for node in adjM[p]:
#         #             inDegree[node] -= 1
#         #             if inDegree[node] == 0:
#         #                 q.append(node)

#         #         res.append(p) 

#         # return res if len(res) == numCourses else []


#         # Recursive DFS -- REDO for amazon 
#         # Time - O(E + V)
#         # Space - O(E + V)

#         # adjM = {i:[] for i in range(numCourses)}

#         # for p in prerequisites:
#         #     adjM[p[0]].append(p[1])

#         # res = []
#         # cycle = set() 
#         # visit = set()


#         # def dfs(node):
#         #     if node in cycle:
#         #         return False

#         #     if node in visit:
#         #         return True

#         #     cycle.add(node)

#         #     for n in adjM[node]:
#         #         if not dfs(n):
#         #             return False

#         #     cycle.remove(node)

#         #     visit.add(node)
#         #     res.append(node)

#         #     return True

#         # for i in range(numCourses):
#         #     if not dfs(i):
#         #         return []

#         # return res

        

        adj_list = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        res = []

        for p in prerequisites:
            adj_list[p[1]].append(p[0])
            in_degree[p[0]] += 1

        q = collections.deque()

        for c in range(numCourses):
            if in_degree[c] == 0:
                q.append(c)

        while q:
            node = q.popleft()
            res.append(node)

            for neigh in adj_list[node]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    q.append(neigh)

        if len(res) == numCourses:
            return res

        return []

