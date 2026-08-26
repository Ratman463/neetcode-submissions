class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toHashStr(s: str) -> str:
            a = [0]*26
            resStr = ""
            delimeter = "*"
            for i in range(len(s)):
                index = ord(s[i]) - ord('a')
                a[index] += 1

            for i in range(len(a)):
                resStr += str(a[i])
                resStr += delimeter
            return resStr

        dick: Dict[str, List[str]] = {}
        
        for s in strs:
            hash = toHashStr(s)
            if dick.get(hash):
                dick[hash].append(s)
            else:
                dick[hash] = [s]

        res = []

        for d in dick:
            res.append(dick[d])

        return res
    
        