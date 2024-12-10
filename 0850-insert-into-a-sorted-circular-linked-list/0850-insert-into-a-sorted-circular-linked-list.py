"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        # Solution 1 - Two pointers
        # Time - O(N)
        # Space - O(1)

        # Intuition - Understand that it in increasing order but also in circular fashion
        # So your head could be any of the element in the increasing order


        # if not head:  # Case 1 : if the head is empty
        #     new_node = Node(insertVal)
        #     new_node.next = new_node
        #     return new_node

        # cur = head

        # while cur.next != head:
        #     if cur.val <= insertVal <= cur.next.val:
        #         new_node = Node(insertVal, cur.next)
        #         cur.next = new_node
        #         return head
        #     elif cur.val > cur.next.val:  # We have found the end of the increasing order
        #         if insertVal > cur.val or insertVal < cur.next.val:
        #             new_node = Node(insertVal, cur.next)
        #             cur.next = new_node
        #             return head
        #     cur = cur.next

        # Case 2: Insert at the end of the tail
        # new_node = Node(insertVal, cur.next)
        # cur.next = new_node

        # return head




        # Re-do for the interview
        # Time - O(n)
        # Space - O(1)


        if not head:
            new_head = Node(insertVal)
            new_head.next = new_head
            return new_head

        cur = head


        while cur.next != head:
            if cur.val <= insertVal <= cur.next.val:
                cur.next = Node(insertVal, cur.next) 
                return head

            elif cur.val > cur.next.val: # reached the end of increasing order
                if insertVal > cur.val or insertVal < cur.next.val:
                    cur.next = Node(insertVal, cur.next) 
                    return head

            cur = cur.next

        cur.next = Node(insertVal, cur.next) 
        return head


        # NOTE: 
        # For something like [3,4,1] and insert 2, our curr reaches 1 and then breaks as curr.next is now 3.
        # For this case the outside is where you are adding the node


