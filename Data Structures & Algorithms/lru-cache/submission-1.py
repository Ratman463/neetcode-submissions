class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dick = {}
        self.usedDick = []

    def get(self, key: int) -> int:
        res = self.dick.get(key, -1)
        if res != -1:
            if key in self.usedDick:
                self.usedDick.remove(key)
            self.usedDick.append(key)
        return res

    def put(self, key: int, value: int) -> None:

        if key in self.usedDick:
            self.usedDick.remove(key)
        self.usedDick.append(key)
        # print(self.usedDick)

        if len(self.dick) == self.capacity and self.dick.get(key, -1) == -1:
            # full
            needRemove = self.usedDick.pop(0)
            self.dick.pop(needRemove)

        self.dick[key] = value