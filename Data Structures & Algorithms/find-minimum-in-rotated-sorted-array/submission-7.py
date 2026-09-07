class Solution:
    min_uwa_breast = 1001

    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + int((right - left) / 2)
        self.min_uwa_breast = nums[0]

        while left < right:
            self.min_uwa_breast = min(self.min_uwa_breast, nums[mid],nums[left], nums[right])
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid
            mid = left + int((right - left) / 2)
        
        return self.min_uwa_breast