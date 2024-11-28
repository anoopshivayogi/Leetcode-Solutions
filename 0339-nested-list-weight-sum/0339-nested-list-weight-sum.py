# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        # Solution 1 - Using BFS with depth count
        # Time - O(N) - BFS normal time complexity
        # Space - O(N) - BFS normal time complexity 

        # depth = 1

        # from collections import deque

        # q = deque(nestedList)
        # res = 0

        # while q:
        #     for _ in range(len(q)):
        #         if q[0].isInteger():
        #             res += (q.popleft().getInteger() * depth)
        #         else:
        #             q.extend(q.popleft().getList())

        #     depth += 1

        # return res


        # Dry-run
        # [6]
        # depth = 3
        # res = 27


        # Re-do for the interview - Using stack iterative method
        # if N is the depth of the nestedList then;
        # Time - O(n) - Each depth will be nestedList and will be visited once and so are all of its elements
        # Space - O(n) - At one point the stack will have the depth number of items


        # st = [(item, 1) for item in nestedList]
        # res = 0

        # while st:

        #     cur, depth = st.pop()

        #     if cur.isInteger():
        #         res += cur.getInteger() * depth
        #     else:
        #         for item in cur.getList():
        #             st.append((item, depth + 1))

        # return res


        # Re-Do BFS style
        # Time - O(N) - Each nestedList is put into queue and removed from the queue exactly once
        # Space - O(N) - Flat layer - worst case scenario where most of the elements is in single layer then we put all these elements into the queue at the same time
        # for example: q = [1, 2, 3, 4, 5]

        q = collections.deque(nestedList)
        depth = 1
        res = 0

        while q:

            for _ in range(len(q)):
                cur = q.popleft()

                if cur.isInteger():
                    res += (cur.getInteger() * depth)
                else:
                    q.extend(cur.getList())
            depth += 1

        return res