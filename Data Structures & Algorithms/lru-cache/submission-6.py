class Node:
    def __init__(self, val: int, key: int, next: Optional['Node'] = None, pre: Optional['Node'] = None) -> None:
        self.val = val
        self.key = key
        self.next = next
        self.pre = pre

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dick = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def __print_dick(self) -> None:
        print([self.dick[key].val for key in self.dick])

    def __remove(self, node: Node) -> None:
        preNode = node.pre
        nextNode = node.next
        
        if preNode is not None:
            preNode.next = nextNode
        
        if nextNode is not None:
            nextNode.pre = preNode
        
    def __add_to_head(self, node: Node) -> None:
        oldHead = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = oldHead
        if oldHead is not None:
            oldHead.pre = node

    def get(self, key: int) -> int:
        res = self.dick.get(key, -1)
        if res == -1:
            return -1
        else:
            # LRU - move to head
            self.__remove(res)
            self.__add_to_head(res)


            return res.val

    def put(self, key: int, value: int) -> None:
        if key in self.dick:
            node = self.dick[key]
            node.val = value
            self.__remove(node)
            self.__add_to_head(node)
        else:
            node = Node(value, key)
            self.dick[key] = node
            self.__add_to_head(node)
            if len(self.dick) > self.capacity:
                lru = self.tail.pre
                self.__remove(lru)
                del self.dick[lru.key]

