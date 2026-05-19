class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        [i, j] = [0, 0]
        [m, n] = [len(matrix), len(matrix[0])]
        visited = [[False]*n for _ in range(m)]
        res = []
        direction = 'r'

        while True:
            hasRight = not visited[i][j+1] if j+1 < n else False
            hasDown = not visited[i+1][j] if i+1 < m else False
            hasLeft = not visited[i][j-1] if j-1 >= 0 else False
            hasUp = not visited[i-1][j] if i-1 >= 0 else False
            
            
            if not visited[i][j]:
                res.append(matrix[i][j])
                visited[i][j] = True

            if hasRight or hasDown or hasLeft or hasUp:
                if direction == 'r':
                    if hasRight:
                        j += 1
                    else:
                        direction = 'd'

                elif direction == 'd':
                    if hasDown:
                        i += 1
                    else: 
                        direction = 'l'

                elif direction == 'l':
                    if hasLeft:
                        j -= 1
                    else:
                        direction = 'u'
                elif direction == 'u':
                    if hasUp:
                        i -= 1
                    else:
                        direction = 'r'
                else:
                    return res
            
            else:
                return res