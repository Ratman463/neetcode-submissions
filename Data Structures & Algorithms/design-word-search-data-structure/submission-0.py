class WordDictionary:

    def __init__(self):
        self.wordDict: dict[str, dict] = {}
        self.endChar = '@'

    def addWord(self, word: str) -> None:
        d = self.wordDict
        for chr in word:
            d.setdefault(chr, {})
            d = d[chr]
        d[self.endChar] = {} 
        # self.print_dict(self.wordDict)
        
    def search(self, word: str) -> bool:
        d = self.wordDict.copy()
        for chr in word:
            if chr == '.':
                new_dict = {}
                for k in d:
                    for key in d[k]:
                        new_dict[key] = d[k][key]
                d = new_dict
            elif chr in d:
                d = d[chr]
            else:
                return False
        return self.endChar in d
    
    def print_dict(self, d: dict) -> None:
        for key in d:
            if isinstance(d[key], dict) and len(d[key]) > 0:
                self.print_dict(d[key])
            else:
                print(key)