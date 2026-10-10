# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

    
        second = slow.next
        prev = slow.next = None

        while second:
            nxt = second.next
            second.next =prev

            prev = second
            second = nxt

        second = prev

        while second:
            temp1, temp2 = head.next, second.next

            head.next = second
            second.next = temp1

            head = second.next
            second = temp2

