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
            stack.append(cur.val)
            cur = cur.next

        cur = head
        n = len(stack)

        print([x for x in stack])

        for i in range(1,n):
            j = n-1-(i//2) if i%2 == 1 else i//2
            #print(f"j:{j}")
            if i % 2 == 1:
                #print(stack[n-i].val)
                cur.next = ListNode(stack[j])
            else:
                #print(stack[i-1].val)
                cur.next = ListNode(stack[j])
            cur = cur.next
                    
