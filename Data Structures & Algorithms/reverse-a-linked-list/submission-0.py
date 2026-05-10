# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        aux = []
        current = head
        while current is not None:
            aux.append(current.val)
            current = current.next
        
        reversedList = ListNode(-1)
        current = reversedList
        n = len(aux)
        for i in range(n):
            newNode = ListNode(aux[n - 1 - i])
            current.next = newNode
            current = current.next
        return reversedList.next