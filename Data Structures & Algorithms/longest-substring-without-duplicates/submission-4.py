class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def isStringNotDuplicate(s: str, char_set: set) -> bool:
            return len(char_set) == len(s)
        
        i = 0
        maxlen = 0
        char_set = set()

        for j in range(len(s)):
            # print(f"before add: {char_set}")
            char_set.add(s[j])
            # print(j)
            # print(char_set)
            
            if isStringNotDuplicate(s[i:j+1], char_set):
                maxlen = max(maxlen, len(s[i:j+1]))
            else:
                while s[j] in char_set:
                    char_set.remove(s[i])
                    i += 1
                char_set.add(s[j])
        return maxlen
    