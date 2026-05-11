# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        if cur is None:
            return cur

        while cur is not None:
            tmp = cur.next # store next node
            cur.next = prev
            prev = cur
            cur = tmp
        return prev