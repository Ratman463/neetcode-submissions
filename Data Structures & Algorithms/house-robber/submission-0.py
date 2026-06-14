class Solution:
    def rob(self, nums: List[int]) -> int:
        # f[n] = rob most 0...n
        # f[n] = max(f[n-2] + nums[n], f[n-1])
        n = len(nums)
        f = [0] * n
        if n <= 1:
            return nums[0]
        
        f[0] = nums[0]
        

        f[1] = max(nums[0], nums[1])
        for i in range(2,n):
            f[i] = max(f[i-2] + nums[i], f[i-1])
        return f[-1]

        