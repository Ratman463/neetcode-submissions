class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        solution: List[List[str]] = []
        
        def backtrack(board: List[str], row: int) -> None:
            if row == n:
                solution.append(board.copy())

            # try to place queen in row:
            for col in range(n):
                if(isValidPosition(board, row, col)):
                    tmp = board[row]
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                    backtrack(board, row + 1)
                    board[row] = tmp

        def isValidPosition(board: List[str], row: int, col: int) -> bool:
            n = len(board)
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 'Q':
                        if row == i or col == j or abs(row - i) == abs(col - j):
                            return False
            return True

        b = ["."*n for _ in range(n)]
        backtrack(b, 0)
        return solution