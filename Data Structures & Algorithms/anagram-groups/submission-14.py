from _collections_abc import dict_values
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toHash(s: str) -> tuple:
            return tuple(c.get(chr(ord('a') + i), 0) for i in range(26))

        dick: Dict[tuple, List[str]] = {}
        for s in strs:
            c = Counter(s)
            dick.setdefault(tuple(c.get(chr(ord('a') + i), 0) for i in range(26)), []).append(s)
        
        return list(dick.values())