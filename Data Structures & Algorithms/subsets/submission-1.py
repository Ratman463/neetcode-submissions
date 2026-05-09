class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subs(nums: List[int]) -> List[List[int]]:
            if len(nums) == 0:
                return []
            elif len(nums) == 1:
                return [[], [nums[0]]]
            return [*[x for x in subs(nums[1:len(nums)])], 
            *[[nums[0], *x] for x in subs(nums[1:len(nums)])]]

        return subs(nums)