# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Solution 1 - Using hashset
        # m is the number in nums and n is the number of nodes in the linkedlist
        # Time - O(n)
        # Space - O(m)

        # dummy -> 1 -> 2 -> 3 -> 4 -> 5

        remove = set(nums)
        dummy = ListNode()
        dummy.next = head
        cur = dummy

        while cur.next:
            if cur.next.val in remove:
                cur.next = cur.next.next
            else:
                cur = cur.next     

        return dummy.next
