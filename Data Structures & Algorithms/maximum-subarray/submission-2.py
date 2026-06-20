class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        tmp, maxSum = 0, nums[0]
        
        for j in range(n):
            tmp = nums[j] if tmp <= 0 else tmp + nums[j]
            maxSum = max(maxSum, tmp)
        
        return maxSum