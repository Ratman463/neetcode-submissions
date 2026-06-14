# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # p1 -> 0  p2 -> last
        if not head:
            return head
            
        stack = []

        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        cur = head
        n = len(stack)

        for i in range(1,n):
            j = n-1-(i//2) if i%2 == 1 else i//2
            # print(f"j:{j}")
            stack[j].next = None
            # print(stack[j].val)
            cur.next = stack[j]
            cur = cur.next
                    
