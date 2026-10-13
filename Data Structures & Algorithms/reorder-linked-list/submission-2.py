# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = head 
        r = head
        while r and r.next:
            l = l.next
            r = r.next.next

        new = l.next
        l.next = None

        prev = None
        while new:
            nxt = new.next
            new.next = prev

            prev = new
            new = nxt
        
        dummy = ListNode()
        pt = dummy

        l = head
        r = prev
        
        while r:
            lnxt = l.next
            rnxt = r.next

            l.next = r
            r.next = lnxt

            l = l.next.next

            r = rnxt

        


