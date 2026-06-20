class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        [i,j] = [0,0]
        [tmp, maxSum] = [nums[0], nums[0]]

        while j < n:
            if tmp <= 0:
                j += 1
                i = j
                if j < n:
                    tmp = nums[j]
                    maxSum = max(maxSum, tmp)
            else:
                j += 1
                if j < n:
                    tmp += nums[j]
                maxSum = max(maxSum, tmp)
        return maxSum
