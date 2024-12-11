"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Solution 1 - using DFS
        # Time - O(E+V)
        # Space - O(E) - Stack space

        # if not node:
        #     return node

        # mapping = dict()

        # def dfs(node):
        #     if node in mapping:
        #         return mapping[node]

        #     copy = Node(node.val)
        #     mapping[node] = copy

        #     for each_n in node.neighbors:
        #         copy.neighbors.append(dfs(each_n))

        #     return copy


        # return dfs(node)


        # if not node:
        #     return node

        # mapping = {}

        # def dfs(node):
        #     if node in mapping:
        #         return mapping[node]

        #     copy = Node(node.val)
        #     mapping[node] = copy

        #     for n in node.neighbors:
        #         copy.neighbors.append(dfs(n))

        #     return copy

        # return dfs(node)


        # Solution 2 - using BFS
        # Time - O(E+V)
        # Space - O(E+V)

        # if not node:
        #     return node

        # mapping = {}

        # from collections import deque

        # q = deque()
        # q.append(node)
        # mapping[node] = Node(node.val)

        # while q:
        #     popped = q.popleft()

        #     for n in popped.neighbors:
        #         if n not in mapping:
        #             mapping[n] = Node(n.val)
        #             mapping[popped].neighbors.append(mapping[n])
        #             q.append(n)
        #         else:
        #             mapping[popped].neighbors.append(mapping[n])

        # return mapping[node]


        # from collections import deque

        # if not node:
        #     return node

        # mapping = {}
        # q = deque()
        # q.append(node)
        # mapping[node] = Node(node.val)

        # while q:
        #     cur_node = q.popleft()

        #     for neigh in cur_node.neighbors:
        #         if neigh in mapping:
        #             mapping[cur_node].neighbors.append(mapping[neigh])
        #         else:
        #             newNode = Node(neigh.val)
        #             mapping[neigh] = newNode
        #             mapping[cur_node].neighbors.append(mapping[neigh])
        #             q.append(neigh)

        # return mapping[node]


        # Re-do for the interview
        # Time - O(N)
        # Space - O(N)

        if not node:  # NOTE: Think about this edge case
            return node

        mapping = {}

        def clone(node):
            if node in mapping:
                return mapping[node]

            new_node = Node(node.val)
            mapping[node] = new_node

            for neigh in node.neighbors:
                new_node.neighbors.append(clone(neigh))

            return new_node

        clone(node)

        return mapping[node]