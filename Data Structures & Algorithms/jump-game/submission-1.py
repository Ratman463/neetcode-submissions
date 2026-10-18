class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_can_jump = [0] * n
        

        for i in range(n):
            max_can_jump[i] = max(max_can_jump[i-1], nums[i] + i)
            # next cannot reach!
            print(max_can_jump[i] - i)
            if max_can_jump[i] <= i and i < n - 1:
                return False
        
        return max_can_jump[-1] >= nums[-1]