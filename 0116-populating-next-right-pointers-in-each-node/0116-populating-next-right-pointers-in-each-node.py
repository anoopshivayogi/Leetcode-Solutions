"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # Solution 1 - BFS going level by level to connect the nodes 
        # https://www.youtube.com/watch?v=U4hFQCa1Cq0
        # Time - O(n)
        # Space - O(n)

        # if not root:
        #     return root

        # q = collections.deque()
        # q.append(root)

        # while q:
            
        #     q_len = len(q)
        #     for i in range(q_len):
        #         cur_node = q.popleft()

        #         if i < q_len - 1:  # NOTE: one less than the last
        #             cur_node.next = q[0]
                
        #         if cur_node.left:
        #             q.append(cur_node.left)

        #         if cur_node.right:
        #             q.append(cur_node.right)

        # return root


        # NOTE: Followup will come that you have to do this with O(1) space excluding recursion stack

        # Solution 2 - Brilliant solution; Must do !!
        # Time - O(n)
        # Space - O(1)

        # cur, nxt = root, root.left if root else None

        # while cur and nxt:
        #     cur.left.next = cur.right

        #     if cur.next: # If cur.next is not null only then you have to do this 
        #         cur.right.next = cur.next.left

        #     cur = cur.next

        #     if not cur:   # Go to the next level if there is nothing on the right
        #         cur = nxt
        #         nxt = cur.left

        # return root


        # Dry-run 
        # root = 1
        #                   1

        #           2                3   
        #                   ->
        #      4         5       6       7
        #           ->      ->       ->
        # cur = 4
        # nxt = None.  Exited while loop


        # Re-do for the interview
        # Time - O(n)
        # Space - O(1)

        if not root:
            return None

        cur, nxt = root, root.left


        while cur and nxt:
            cur.left.next = cur.right

            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next

            if not cur:
                cur = nxt
                nxt = cur.left

        return root