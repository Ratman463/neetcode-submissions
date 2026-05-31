class PrefixTree:

    dick = {}

    def __init__(self):
        self.dick = {}

    def insert(self, word: str) -> None:
        cur = self.dick
        for chr in word:
            if cur.get(chr):
                cur = cur[chr]
            else:
                cur[chr] = {}
                cur = cur[chr]
        cur[None] = True        

    def search(self, word: str) -> bool:
        cur = self.dick
        for w in word:
            if cur.get(w):
                cur = cur[w]
            else:
                return False
        
        if cur.get(None):
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.dick
        for w in prefix:
            if cur.get(w):
                cur = cur[w]
            else:
                return False
        
        return True