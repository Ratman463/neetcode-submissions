# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # find mid
        slow: ListNode = head
        fast: ListNode = head

        while fast and fast.next and slow and slow.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.val)

        second = slow.next
        slow.next = None

        # reverse last half
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev

        f, s = head, second
        while s and f:
            t1, t2 = f.next, s.next
            f.next = s
            s.next = t1
            f, s = t1, t2

           
