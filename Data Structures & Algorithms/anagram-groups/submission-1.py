class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_str: Dict[str, List[str]] = {}
        ans: List[List[str]] = []

        for i in range(len(strs)):
            string = strs[i]
            countStr = Solution.toCountStr(string)
            if(dict_str.get(countStr) == None):
                dict_str[countStr] = [string]
            else:
                dict_str[countStr].append(string)

        for key in dict_str:
            print(key)
            ans.append(dict_str.get(key, []))
        
        return ans

    @staticmethod
    def toCountStr(string: str) -> str:
        begin = ord('a')
        res = [0] * 26
        resStr = ""
        for i in range(len(string)):
            index = ord(string[i]) - begin
            res[index] += 1

        for i in range(len(res)):
            resStr += chr(res[i])
        
        return resStr

