# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Solution 1 - just solving it using elementary math 
        # Time - O(m + n)
        # Space - O(1)


        # carry = False
        # res = ListNode()
        # curr = res

        # while l1 or l2:
        #     s = 0

        #     if l1:
        #         s += l1.val

        #     if l2:
        #         s += l2.val

        #     if carry:
        #         s += 1

        #     if s > 9:
        #         carry = True
        #         s = s % 10
        #     else:
        #         carry = False

        #     newNode = ListNode(s)
        #     curr.next = newNode
        #     curr = curr.next

        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next


        # if carry:
        #     newNode = ListNode(1)
        #     curr.next = newNode
        #     curr = curr.next

        # curr.next = None


        # return res.next


        # Solution 2 - more elegant solution 


        # dummy = ListNode()
        # curr = dummy

        # carry = 0

        # while l1 or l2 or carry:
        #     v1 = l1.val if l1 else 0
        #     v2 = l2.val if l2 else 0

        #     val = v1 + v2 + carry

        #     carry = val // 10
        #     val = val % 10

        #     curr.next = ListNode(val)
        #     curr = curr.next

        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None

        # return dummy.next


        # Re-Do for the interview
        # Time - O(m + n)
        # Space - O(1)


        # carry = 0
        # res = ListNode()
        # curr = res

        # while l1 or l2 or carry:
        #     l1_val = l1.val if l1 else 0
        #     l2_val = l2.val if l2 else 0

        #     total = l1_val + l2_val + carry

        #     carry = total // 10
        #     val = total % 10
        
        #     curr.next = ListNode(val)
        #     curr = curr.next

        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None

        # return res.next


        carry = 0
        res = ListNode(-1)
        curr = res

        while carry or l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            val = total % 10

            new_node = ListNode(val)
            curr.next = new_node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return res.next