class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toHashStr(s: str) -> str:
            a = [0]*26
            delimeter = "*"
            for i in range(len(s)):
                index = ord(s[i]) - ord('a')
                a[index] += 1
            return "".join(str(x) + delimeter for x in a)

        dick: Dict[str, List[str]] = {}
        
        for s in strs:
            hash = toHashStr(s)
            dick.setdefault(hash, []).append(s)

        res = []

        for d in dick:
            res.append(dick[d])

        return res
    
        