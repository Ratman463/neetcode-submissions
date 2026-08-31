"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(-1)
        cur1 = head
        cur2 = newHead
        cur3 = head

        dick = {}

        while cur1:
            dick[cur1] = Node(cur1.val)
            cur1 = cur1.next
            
        while cur3 and cur3.next:
            newNode = dick.get(cur3, None)
            newNode.next = dick.get(cur3.next, None)
            newNode.random = dick.get(cur3.random, None)           
            cur2.next = newNode
            cur2 = cur2.next
            cur3 = cur3.next

        if(cur3):
            newNode = dick.get(cur3, None)
            newNode.next = None
            newNode.random = dick.get(cur3.random, None)    
            cur2.next = newNode
            
        return newHead.next