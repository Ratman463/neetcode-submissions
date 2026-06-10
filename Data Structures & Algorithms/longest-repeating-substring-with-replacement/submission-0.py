class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        maxfreq = 0
        left = 0
        res = 0

        for right in range(len(s)):
            chr = ord(s[right]) - ord('A')
            freq[chr] += 1
            maxfreq = max(maxfreq, freq[chr])

            window_len = right - left + 1
            if (window_len - maxfreq) > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            res = max(right - left + 1, res)
        return res