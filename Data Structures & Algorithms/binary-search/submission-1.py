class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(start: int, end: int) -> int:
            if start > end or end >= len(nums):
                return -1
            
            mid = (start + end) // 2

            if nums[mid] == target:    
                return mid
            else:
                m = binarysearch(start, mid - 1)
                n = binarysearch(mid + 1, end)
                return m if m >= 0 else n
        return binarysearch(0, len(nums)-1)