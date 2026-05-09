class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_one(n: int) -> int:
            cnt = 0
            while n > 0:
                cnt += 1 if n & 1 == 1 else 0
                n = n >> 1
            return cnt
        return [count_one(x) for x in range(n+1)]