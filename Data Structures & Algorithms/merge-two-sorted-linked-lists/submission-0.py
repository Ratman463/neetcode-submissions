# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = ListNode(-1)
        p1.next = list1
        p2 = list2
        head = p1

        while p2 is not None:
            if p1.next is not None:
                if p1.next.val > p2.val:
                    tmp = p1.next
                    p1.next = ListNode(p2.val)
                    p1 = p1.next
                    p1.next = tmp
                    p2 = p2.next
                else:
                    p1 = p1.next
            else:
                p1.next = p2
                return head.next
                
        return head.next