class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.myPowPostive(x, n) if n >= 0 else 1 / self.myPowPostive(x, -n) 
        
    def myPowPostive(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            tmp = self.myPowPostive(x, n // 2)
            return tmp * tmp
        else:
            tmp = self.myPowPostive(x, (n - 1) // 2)
            return x * tmp * tmp