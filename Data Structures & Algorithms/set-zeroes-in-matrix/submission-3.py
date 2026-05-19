class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        [hasRowZero, hasColZero] = [False, False]
        for i in range(0, m):
            if matrix[i][0] == 0:
                hasRowZero = True
        for j in range(0, n):
            if matrix[0][j] == 0:
                hasColZero = True

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        

        for i in range(0,m):
            if hasRowZero:
                matrix[i][0] = 0
        for j in range(0,n):
            if hasColZero:
                matrix[0][j] = 0