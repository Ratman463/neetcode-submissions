class Solution:
    splitter = '🍉'
    def encode(self, strs: List[str]) -> str:
        return self.splitter.join(strs) + self.splitter if len(strs) > 0 else ""

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0
        while j < len(s):
            if(s[j] == '🍉'):
                if(j>i):
                    res.append(s[i:j])
                else:
                    res.append("")
                i=j+1
                j=i
            else:
                j+=1
        return res
