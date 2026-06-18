class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for str1 in strs:
            hasharr = [0] * 26
            hashstr = ""
            for chr in str1:
                hasharr[ord(chr) - ord('a')] += 1
            for num in range(len(hasharr)):
                hashstr = hashstr + "*" + str(hasharr[num])
            if d.get(hashstr):
                d[hashstr].append(str1)
            else:
                d[hashstr] = [str1]

        
        for pairs in d:
            #print(d[pairs])
            res.append(d[pairs])

        return res

