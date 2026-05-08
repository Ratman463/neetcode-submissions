class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def isStringNotDuplicate(s: str) -> bool:
            return len(set(s)) == len(s)
        
        i = 0
        maxlen = 0
        for j in range(len(s)):
            if isStringNotDuplicate(s[i:j+1]):
                # print(f"s[i:j+1]:{s[i:j+1]}")
                maxlen = max(maxlen, len(s[i:j+1]))
            else:
                i += 1
        return maxlen
    