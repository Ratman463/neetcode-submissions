# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        cur = res
        inc = 0
        while l1 or l2:
            next_val = 0

            if l1:
                next_val += l1.val
                l1 = l1.next
            if l2:
                next_val += l2.val
                l2 = l2.next

            nextNode = None;
            # print(next_val)
            if next_val + inc >= 10:
                next_val = next_val + inc - 10
                nextNode = ListNode(next_val)
                inc = 1
            else:
                nextNode = ListNode(next_val + inc)
                inc = 0

            cur.next = nextNode
            cur = cur.next
        
        if inc == 1:
            cur.next = ListNode(inc)

        return res.next