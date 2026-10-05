# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(-1)
        k = len(lists)
        s = [x for x in lists if isinstance(x, ListNode)]
        s.sort(key= lambda x: x.val)

        cur = head
        while len(s) > 0:
            small = s.pop(0)
            cur.next = ListNode(small.val)
            cur = cur.next
            
            smallest_val = small.val
            small = small.next
        
            if isinstance(small, ListNode):
                # insert new
                inserted = False
                for i in range(len(s)):
                    if small.val < s[i].val:
                        s.insert(i, small)
                        inserted = True
                        break
                if not inserted:
                    s.append(small)
            
        return head.next
