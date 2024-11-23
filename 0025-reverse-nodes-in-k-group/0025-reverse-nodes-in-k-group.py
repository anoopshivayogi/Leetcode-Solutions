# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Solution 1 - Using 
        # Time - O(n)
        # Space - O(1)

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth_node = self.get_kth(group_prev, k)

            if not kth_node:
                return dummy.next

            group_next = kth_node.next

            prev, curr = group_next, group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp


            temp = group_prev.next
            group_prev.next = kth_node
            group_prev = temp


    def get_kth(self, head, k):

        while k and head:
            head = head.next
            k -= 1

        return head