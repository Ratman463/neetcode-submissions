class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        if m == 0:
            return n
        elif n == 0:
            return m
            
        dp = [[0]*n for _ in range(m)]

        # f(2,2): mo -> mo 0 
        # f(3,2): mon -> mo 1
        # f(2,3): mo -> mon 1
        # f(3,3): mon -> mon 0
        # 状态转移: f(m, n) = min(f(m-1, n-1) + ..., f(m-1, n) + 1, f(m, n-1) + 1

        for i in range(m):
            for j in range(n):
                flag = 0 if word1[i] == word2[j] else 1
                if i == 0 and j == 0:
                    dp[i][j] = flag
                elif i == 0 and j > 0:
                    dp[i][j] = flag + dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] = flag + dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + flag, dp[i-1][j] + 1, dp[i][j-1] + 1)

        return dp[m-1][n-1]
