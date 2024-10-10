# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Solution 1 - Using log(n) extra space
        # Time - 
        # Space - 


        if not head or not head.next:
            return head

        mid = self.get_mid(head)
        right = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(right)

        return self.merge(left, right)


    def get_mid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


    def merge(self, left, right):
        new_head = ListNode()
        cur_node = new_head

        while left and right:
            
            if left.val <= right.val:
                cur_node.next = left
                left = left.next
            else:
                cur_node.next = right
                right = right.next

            cur_node = cur_node.next

        if left:
            cur_node.next = left

        if right:
            cur_node.next = right

        return new_head.next
