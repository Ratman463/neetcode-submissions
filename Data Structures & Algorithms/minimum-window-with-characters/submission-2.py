class Solution:


    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)          # t 每个字符需要几个
        window = Counter()         # 窗口里现有哪些
        have = 0                   # 已经有几个种类达标了
        need_total = len(need)     # 一共几个种类
        l = 0
        res = ""
        min_len = float('inf')

        for r, ch in enumerate(s):
            window[ch] += 1
            if window[ch] == need[ch]:     # 这个字符刚好凑够 → 达标
                have += 1

            while have == need_total:      # 全部达标 = 满足 → 收缩求最短
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r + 1]       # 记录答案
                out = s[l]
                window[out] -= 1
                if window[out] < need[out]:  # 去掉这个字符后不达标了 → 破坏满足
                    have -= 1
                l += 1
        return res
        