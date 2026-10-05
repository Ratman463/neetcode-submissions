# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def merge2Lists(self, listA: Optional[ListNode], listB: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cur = head
        while listA or listB:
            if listA is None:
                cur.next = listB
                break
            elif listB is None:
                cur.next = listA
                break
            else:
                valA = listA.val
                valB = listB.val
                if valA < valB:
                    cur.next = listA
                    listA = listA.next
                else:
                    cur.next = listB
                    listB = listB.next
                cur = cur.next
        return head.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       
        k = len(lists)
 
        if k == 0:
            return None
        elif k == 1:
            return lists[0]
        elif k == 2:
            return self.merge2Lists(listA=lists[0], listB=lists[1])
        else:
            return self.merge2Lists(self.mergeKLists(lists[0:k//2]), self.mergeKLists(lists[k//2:k]))
        return None