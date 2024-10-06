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
        # Time - O(n)
        # Space - O(n)

        if not root:
            return root

        q = collections.deque()
        q.append(root)

        while q:
            
            count = len(q)
            for _ in range(len(q)):
                cur_node = q.popleft()

                if count > 1:
                    cur_node.next = q[0]
                    count -= 1
                
                if cur_node.left:
                    q.append(cur_node.left)

                if cur_node.right:
                    q.append(cur_node.right)

        return root