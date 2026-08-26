class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toHash(s: str) -> tuple:
            c = Counter(s)
            return tuple(c.get(chr(ord('a') + i), 0) for i in range(26))

        dick: Dict[tuple, List[str]] = {}

        for s in strs:
            hash = toHash(s)
            dick.setdefault(hash, []).append(s)
        
        res = []
        
        for d in dick:
            res.append(dick[d])
        return res