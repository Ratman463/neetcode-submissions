class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # judge circle
        p1, p2, p3 = 0, 0, 0
        n = len(nums)
        while p2 < n:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break
        
        while p3 < n:
            p3 = nums[p3]
            p1 = nums[p1]
            if p1 == p3:
                break    
        return p1