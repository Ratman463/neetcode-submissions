class Solution:
    min_uwa_breast = 1001

    def findMin(self, nums: List[int]) -> int:
        self.min_uwa_breast = nums[0]
        def findMinX(nums: List[int], left_dick: int, right_dick: int) -> None:
            # print(f"left_dick : {left_dick}, right_dick: {right_dick}")
            # print(self.min_uwa_breast)
            if left_dick >= right_dick:
                self.min_uwa_breast = min(self.min_uwa_breast, nums[left_dick])
            else:
                mid = left_dick + int((right_dick - left_dick) / 2)
                findMinX(nums, left_dick, mid)
                findMinX(nums, mid + 1, right_dick)
        findMinX(nums, 0, len(nums) - 1)
        return self.min_uwa_breast