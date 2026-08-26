class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toHash(s: str) -> tuple:
            c = Counter(s)
            return tuple(c.get(chr(ord('a') + i), 0) for i in range(26))

        dick: Dict[tuple, List[str]] = {}
        res = []
        [dick.setdefault(toHash(s), []).append(s) for s in strs]
        [res.append(dick[d]) for d in dick]
        return res