class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toHashStr(str_in: str) -> str:
            arr: List[int] = [0] * 26

            for chr in str_in:
                arr[ord(chr) - ord('a')] += 1
            
            res = ''
            for num in arr:
                res += str(num)
                res += '#'

            return res
        
        dict_strs: Dict[str, List[str]] = {}
        groups = []

        for s in strs:
            ss = toHashStr(s)
            # print(ss)
            if dict_strs.get(ss):
                dict_strs[ss].append(s)
            else:
                dict_strs[ss] = [s]
        
        for pairs in dict_strs:
            # print(f"pairs: {pairs}")
            groups.append(dict_strs[pairs])

        return groups
