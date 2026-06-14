class Solution:
    def rob(self, nums: List[int]) -> int:
        # f[n][0] = rob most 0...n with 0
        # f[n][1] = rob most 0...n without 0
        # f[n][0] = max(f[n-1][0], f[n-1][1] + nums[n])
        n = len(nums)
        f = [[0,0] for _ in range(n)]

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        f[0][0], f[0][1] = nums[0], 0
        f[1][0], f[1][1] = nums[0], nums[1]
        for i in range(2,n):
            f[i][0] = max(f[i-1][0], f[i-2][0] + nums[i] if i < n - 1 else 0)
            f[i][1] = max(f[i-1][1], f[i-2][1] + nums[i])
        return max(f[n-1][0], f[n-1][1])