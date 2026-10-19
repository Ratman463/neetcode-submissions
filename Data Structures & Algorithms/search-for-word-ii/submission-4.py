class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # ---------- 1. 建 Trie ----------
        trie = {}
        for w in words:
            node = trie
            for ch in w:
                node = node.setdefault(ch, {})
            node['#'] = w          # 词尾存整词

        m, n = len(board), len(board[0])
        res = []

        # ---------- 2. 一次 DFS 匹配所有词 ----------
        def dfs(i, j, node):
            ch = board[i][j]
            nxt = node.get(ch)
            if nxt is None:                 # 这个方向没有词以 ch 开头 → 剪枝
                return

            if '#' in nxt:                  # 命中一个完整单词
                res.append(nxt.pop('#'))    # pop 顺便去重

            board[i][j] = '#'               # 原地标记已访问
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, nxt)
            board[i][j] = ch                # 回溯，恢复

            if not nxt:                     # 这个节点下的词都找完了 → 从 Trie 剪掉
                node.pop(ch, None)

        # ---------- 3. 每个格子作为起点 ----------
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return res