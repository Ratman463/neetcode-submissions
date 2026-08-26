class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toHashStr(s: str) -> str:
            c = Counter(s)
            return "".join(str(x) + "*" for x in [c.get(chr(ord('a') + i), 0) for i in range(26)])

        dick: Dict[str, List[str]] = {}



        for s in strs:
            hash = toHashStr(s)
            dick.setdefault(hash, []).append(s)
        
        res = []
        
        for d in dick:
            res.append(dick[d])
        return res