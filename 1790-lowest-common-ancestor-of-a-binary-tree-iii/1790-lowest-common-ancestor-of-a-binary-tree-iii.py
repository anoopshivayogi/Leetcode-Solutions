"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        # Solution 1 - Using set
        # Time - O(m + n)
        # Space - O(m)

        # seen = set()

        # while p:
        #     seen.add(p)
        #     p = p.parent


        # while q:
        #     if q in seen:
        #         return q
        #     q = q.parent



        # Solution 2 - Using just pointers - kind of like Tortoise & Hare problem
        # Time - O(n) - Does it not run the number of depth difference between p and q ?
        # Space - O(1)

        # p_copy = p
        # q_copy = q

        # while p_copy != q_copy:
        #     p_copy = p_copy.parent if p_copy.parent else p
        #     q_copy = q_copy.parent if q_copy.parent else q

        # return p_copy


        # Re-do for the interview
        # Time - 
        # Space - 

        # p_copy, q_copy = p, q

        # while p_copy != q_copy:
        #     p_copy = p_copy.parent if p_copy else p
        #     q_copy = q_copy.parent if q_copy else q

        # return p_copy


        # Solution optional
        # Time - 
        # Space - 


        def distance_from_top(node):
            if not node:
                return 0

            return 1 + distance_from_top(node.parent)

        
        p_distance = distance_from_top(p)
        q_distance = distance_from_top(q)

        while p_distance > q_distance:
            p = p.parent
            p_distance -= 1

        while q_distance > p_distance:
            q = q.parent
            q_distance -= 1

        while p != q:
            p = p.parent
            q = q.parent

        return p
