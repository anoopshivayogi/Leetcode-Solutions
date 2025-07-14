# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        # Solution 1 - Just looping through and using 2^(nth node)
        # Time - 
        # Space - 


        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        cur = prev

        count = 0
        res = 0

        while cur:
            if cur.val:
                res += (2 ** count)
            cur = cur.next
            count += 1

        return res
