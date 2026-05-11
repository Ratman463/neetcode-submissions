# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = head
        slow = head
        fast = head
        for _ in range(n):
            if fast:
                fast = fast.next
        
        if fast is None:
            if res:
                return res.next
            else:
                return res

        while fast and slow and fast.next and slow.next:
            slow = slow.next
            fast = fast.next
        
        if slow and slow.next:
            slow.next = slow.next.next

        return res