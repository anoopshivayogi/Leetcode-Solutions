# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        # Solution 1 - Reverse the linkedlist and using 2^(nth node)
        # Time - O(2n)
        # Space - O(1)

        # Reverse a linkedlist
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        cur = prev

        # Traverse and use 2^count
        count = 0
        res = 0

        while cur:
            if cur.val:
                res += (2 ** count)
            cur = cur.next
            count += 1

        return res
