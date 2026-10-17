# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()

        res = dummy

        carry = 0
        while l1 or l2 or carry != 0:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)

            add = l1.val + l2.val + carry
        
            carry = add // 10
            val = add % 10

            res.next = ListNode(val)
            res = res.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


