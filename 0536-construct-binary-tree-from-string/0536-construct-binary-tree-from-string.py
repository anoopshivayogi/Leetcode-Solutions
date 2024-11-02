# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        # Solution 1 - Using stack
        # https://www.youtube.com/watch?v=AY7ZO0Q1s0k
        # Time - O(N)
        # Space - O(N)
        
        # if not s:  # NOTE: Clarify what to return in this case with the interviewer
        #     return None

        # st = []
        # i = 0

        # while i < len(s):
            
        #     if s[i] == "-" or s[i].isdigit():
        #         val = 0
        #         neg = False

        #         if s[i] == "-":
        #             i += 1
        #             neg = True

        #         while i < len(s) and s[i].isdigit():
        #             val = val * 10 + int(s[i])
        #             i += 1

        #         i -= 1

        #         if neg:
        #             cur_node = TreeNode(-val)
        #         else:
        #             cur_node = TreeNode(val)
                
        #         st.append(cur_node)

        #     elif s[i] == ")":

        #         if st:
        #             top = st.pop()

        #             if not st[-1].left:
        #                 st[-1].left = top
        #             else:
        #                 st[-1].right = top

        #     i += 1

        # return st[-1]


        # Solution 2 - Using recursion
        # Time - 
        # Space - 



        def recursion(i):

            if i >= len(s):
                return None, i

            neg = False
            val = 0

            if s[i] == "-":
                neg = True
                i += 1

            while i < len(s) and s[i].isdigit():
                val = val * 10 + int(s[i])
                i += 1

            if neg:
                val *= -1

            node = TreeNode(val)

            if i < len(s) and s[i] == "(":
                node.left, i = recursion(i + 1)
                i += 1  # Skip the )


            if i < len(s) and s[i] == "(":
                node.right, i = recursion(i + 1)
                i += 1  # Skip the )

            return node, i

        return recursion(0)[0]