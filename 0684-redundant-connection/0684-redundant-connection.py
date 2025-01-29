class UnionFind:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.parents = [i for i in range(self.n)]

    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]] # Path compression
            node = self.parents[node]

        return node


    def union(self, n1, n2):
        node1 = self.find(n1)
        node2 = self.find(n2) 

        if node1 == node2:
            return True 

        if self.rank[node1] >= self.rank[node2]:
            self.parents[node2] = node1 
            self.rank[node1] += 1
        else:
            self.parents[node1] = node2
            self.rank[node2] += 1

        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # Solution 1 - Union and find algorithm. very efficient with compression step. 

        # par = [i for i in range(len(edges)+1)]
        # ranks = [1] * (len(edges) + 1)

        # # find the parent of the node
        # def find(n):

        #     while n != par[n]:
        #         par[n] = par[par[n]] # Compression step -> optimization++
        #         n = par[n]
        #     return n
        

        # def union(n1, n2):
        #     p1 = find(n1)
        #     p2 = find(n2)

        #     if p1 == p2:
        #         return False
            
        #     if ranks[p1] > ranks[p2]:
        #         par[p2] = p1
        #         ranks[p1] += 1
        #     else:
        #         par[p1] = p2
        #         ranks[p2] += 1

        #     return True


        # for e in edges:
        #     if not union(e[0], e[1]):
        #         return e




        par = [i for i in range(len(edges)+1)]
        ranks = [1] * (len(edges)+1)


        def find(node):
            while node != par[node]:
                # par[node] = par[par[node]] # Optional compression step 
                node = par[node]

            return node


        def union(e1, e2):
            p1 = find(e1)
            p2 = find(e2)

            if p1 == p2:
                return True

            
            if ranks[p1] >= ranks[p2]:
                par[p2] = p1
                ranks[p1] += 1
            else:
                par[p1] = p2
                ranks[p2] += 1

            return False

            
        for e in edges:
            if union(e[0], e[1]):
                return e
            
             

        













