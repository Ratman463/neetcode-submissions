class Solution:

    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + int((right - left) / 2)

        while left < right:
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            mid = left + int((right - left) / 2)
        return nums[left]