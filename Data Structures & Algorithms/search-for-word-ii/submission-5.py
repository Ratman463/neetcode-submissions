from typing import List
from collections import defaultdict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        HALF = 5

        # paths[s] = [(起点, 终点, 掩码), ...]   枚举所有长度<=5的路径
        paths = defaultdict(list)

        def enum(i, j, cells, mask, s):
            paths[s].append((cells[0], cells[-1], mask))
            if len(cells) == HALF:
                return
            for di, dj in DIRS:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    bit = 1 << (ni * n + nj)
                    if not (mask & bit):                 # 同格不重复
                        enum(ni, nj, cells + [(ni, nj)], mask | bit, s + board[ni][nj])

        for i in range(m):
            for j in range(n):
                enum(i, j, [(i, j)], 1 << (i * n + j), board[i][j])

        def adjacent(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1

        def ok(word):
            L = len(word)
            if L <= HALF:
                return len(paths.get(word, ())) > 0
            L1 = L // 2
            left, right = paths.get(word[:L1]), paths.get(word[L1:])
            if not left or not right:
                return False
            for (ps, pe, pm) in left:
                for (ss, se, sm) in right:
                    if (pm & sm) == 0 and adjacent(pe, ss):   # 不重叠 + 相邻
                        return True
            return False

        return [w for w in words if ok(w)]