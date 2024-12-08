"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Solution 1 - Handling mapping of newNodes to oldNodes using HashMap
        # Time - O(n)
        # Space - O(n)

        # if not head:
        #     return head
        
        # rMap = {None:None} # None:None Saved our day

        # HeadMap = head
        # while HeadMap:
        #     newNode = Node(HeadMap.val, None, None)
        #     rMap[HeadMap] = newNode
        #     HeadMap = HeadMap.next

        
        # traverse = head
        # while traverse:
        #     rMap[traverse].next = rMap[traverse.next]
        #     rMap[traverse].random = rMap[traverse.random]
        #     traverse = traverse.next

        # return rMap[head]


        # Solution 2 - Same solution as above but handling None case differently
        # Time - O(n)
        # Space - O(n)

        # mHead = head

        # mapping = {}

        # while mHead:
        #     newNode = Node(mHead.val)
        #     mapping[mHead] = newNode
        #     mHead = mHead.next
        
        # mHead = head
        
        # while mHead:
        #     mapping[mHead].next = mapping.get(mHead.next, None)
        #     mapping[mHead].random = mapping.get(mHead.random, None)
        #     mHead = mHead.next

        # return mapping.get(head, None)



        # mapping = {None: None}

        # curHead = head


        # while curHead:
        #     newNode = Node(curHead.val)
        #     mapping[curHead] = newNode
        #     curHead = curHead.next

        
        # curHead = head

        # while curHead:
        #     mapping[curHead].next = mapping[curHead.next]
        #     mapping[curHead].random = mapping[curHead.random]
        #     curHead = curHead.next 

        # return mapping[head]





        # Solution 2 - Recursive solution 


        # mapping = {}

        # def dfs(head):
        #     nonlocal mapping

        #     if not head:
        #         return None

        #     if head in mapping:
        #         return mapping[head]
            
        #     print(head.val)

        #     newHead = Node(head.val)
        #     mapping[head] = newHead # Have to store this right away or else you'll recieve recursion depth reached 
        #     newHead.next = dfs(head.next)
        #     newHead.random = dfs(head.random)

        #     return newHead

        # return dfs(head)



        # Re-do for the interview
        # Time - 
        # Space - 


        # mapping = collections.defaultdict(lambda : None)  # old to new-mapping

        # cur = head

        # while cur:
        #     new_node = Node(cur.val)
        #     mapping[cur] = new_node
        #     cur = cur.next

        # cur = head

        # while cur:
        #     mapping[cur].next = mapping[cur.next]
        #     mapping[cur].random = mapping[cur.random]
        #     cur = cur.next

        # return mapping[head]


        # Re-Do

        # mapping = collections.defaultdict(list)

        # mapping[None] = None

        # cur = head

        # while cur:
        #     newNode = Node(cur.val)
        #     mapping[cur] = newNode
        #     cur = cur.next

        # cur = head 


        # while cur:
        #     mapping[cur].next = mapping[cur.next]
        #     mapping[cur].random = mapping[cur.random]
        #     cur = cur.next

        # return mapping[head]


        # NOTE: IMPPP!!. Constant space solution is very important for meta
        # Time - O(n)
        # Space - O(1)


        if not head:  # NOTE: Very important move!!. Always make sure to handle empty inputs
            return None


        curr = head

        # Inserting new cloned node in between the linked list
        # A -> A' -> B -> B' -> C -> C'
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node

            curr = new_node.next

        curr = head

        # Link the random pointers for the cloned nodes
        while curr:
            curr.next.random = curr.random.next if curr.random else None # Handle the case where random node could be None
            curr = curr.next.next


        # Seperate out the old nodes link from the cloned ones
        # A -> A' -> B -> B' -> C -> C'
        # A -> B -> C and A' -> B' -> C'

        old_list_ptr = head
        new_list_ptr = head.next
        new_head = new_list_ptr

        while old_list_ptr:
            old_list_ptr.next = old_list_ptr.next.next
            new_list_ptr.next = new_list_ptr.next.next if new_list_ptr.next else None

            old_list_ptr = old_list_ptr.next
            new_list_ptr = new_list_ptr.next

        return new_head


        

