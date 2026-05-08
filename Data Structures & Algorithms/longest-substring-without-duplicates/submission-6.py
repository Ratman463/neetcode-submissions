class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxlen = 0
        char_set = set()

        for j in range(len(s)):
            char_set.add(s[j])
            if len(char_set) == j-i+1:
                maxlen = max(maxlen, j-i+1)
            else:
                while s[j] in char_set:
                    char_set.remove(s[i])
                    i += 1
                char_set.add(s[j])
        return maxlen
    