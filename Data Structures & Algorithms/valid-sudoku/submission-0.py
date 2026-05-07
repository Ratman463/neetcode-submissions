class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 10
        rows = [[0]*N for _ in range(N)]
        cols = [[0]*N for _ in range(N)]
        blocks = [[0]*N for _ in range(N)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                chr = board[i][j]
                
                if chr != '.':
                    n = int(chr)                    
                    # try to add to rows
                    if rows[i][n] > 0:
                        return False
                    else:
                        rows[i][n] += 1
                    
                    # try to add to cols
                    if cols[j][n] > 0:
                        return False
                    else:
                        cols[j][n] += 1

                    # try to add to blocks
                    block_index = (i//3)*3 + (j//3)
                    if blocks[block_index][n] > 0:
                        return False
                    else:
                        blocks[block_index][n] += 1
        return True