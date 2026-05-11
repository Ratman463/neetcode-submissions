# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t = 0
        cur = head
        while t <= 1000:
            if cur is None:
                return False
            else:
                cur = cur.next
            t += 1

        return True