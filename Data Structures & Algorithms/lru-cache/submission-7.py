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
        resNode = self.dick.get(key, -1)
        tmp = Node(value, key)

        if resNode == -1:
            # not exist
            if len(self.dick) >= self.capacity:
                # need remove last ele
                if self.tail.pre:
                    lru = self.tail.pre
                    self.__remove(self.tail.pre)
                    del self.dick[lru.key]
                self.__add_to_head(tmp)
                
                self.dick[key] = tmp
            else:
                # add new
                self.__add_to_head(tmp)
                self.dick[key] = tmp
        else:
            # exist in dick
            # print(resNode.val)
            resNode.val = value
            self.__remove(resNode)
            self.__add_to_head(resNode)
