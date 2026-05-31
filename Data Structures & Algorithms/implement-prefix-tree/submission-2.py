class PrefixTree:

    def __init__(self):
        self.words = {}

    def insert(self, word: str) -> None:
        cur = self.words
        for chr in word:
            if chr in cur:
                cur = cur[chr]
            else:
                cur[chr] = {}
                cur = cur[chr]
        cur['#'] = True
    
    def startsWithExists(self, prefix: str) -> Optional[dict]:
        cur = self.words
        for w in prefix:
            if w in cur:
                cur = cur[w]
            else:
                return None
        return cur

    def search(self, word: str) -> bool:
        cur = self.startsWithExists(word)

        if cur is not None and '#' in cur:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.startsWithExists(prefix)
        return cur is not None