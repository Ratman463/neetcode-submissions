class Solution:
    def isHappy(self, n: int) -> bool:
        set = []
        sum = 0
        while True:
            res = self.cal_s(n)
            if res == 1:
                return True
            if res in set:
                return False
            set.append(res)
            n = res

    def cal_s(self, n: int) -> int:
        sum = 0
        while n > 0:
            d = n % 10
            n = n // 10
            sum += d * d
        return sum