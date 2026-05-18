class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1

        def rot(s: int) -> None:
            for i in range(n-2*s):
                [
                    matrix[s+i][n-s],
                    matrix[n-s][n-s-i],
                    matrix[n-s-i][s],
                    matrix[s][s+i]
                ] =  [
                    matrix[s][s+i],
                    matrix[s+i][n-s],
                    matrix[n-s][n-s-i],
                    matrix[n-s-i][s]
                ]

        
        for s in range(n // 2 + 1):
            rot(s)