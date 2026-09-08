class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2

        while right > left:
            if nums[mid] > nums[right]:
                # min point between [mid, right]
                left = mid + 1
            else:
                # min point between [left, mid]
                right = mid
            mid = left + (right - left) // 2
        return nums[left]