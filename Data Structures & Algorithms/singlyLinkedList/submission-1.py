class LinkedList:

    ls = []
    
    def __init__(self):
        self.ls = []
    
    def get(self, index: int) -> int:
        return self.ls[index] if index < len(self.ls) else -1

    def insertHead(self, val: int) -> None:
        self.ls = [val, *self.ls]

    def insertTail(self, val: int) -> None:
        self.ls = [*self.ls, val]

    def remove(self, index: int) -> bool:
        n = len(self.ls)
        if index >= n:
            return False
        else:
            self.ls = [*self.ls[:index], *self.ls[index+1:]]
            return True

    def getValues(self) -> List[int]:
        return self.ls