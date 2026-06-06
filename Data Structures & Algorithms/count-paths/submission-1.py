class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0] * n for _ in range(m)]
        if m == 1 or n == 1:
            return 1
        for i in range(m):
            for j in range(n):
                if i == 0:
                    res[i][j] = 1
                elif j == 0:
                    res[i][j] = 1
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1] 
        return res[m-1][n-1]