class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque([])
        n = len(digits)
        inc = 1
        cur = 0

        for i in range(n - 1, -1, -1):
            cur = digits[i] + inc
            if cur >= 10:
                cur -= 10
                inc = 1
            else:
                inc = 0
            res.appendleft(cur)
        if inc == 1:
            res.appendleft(inc)
        return list(res)