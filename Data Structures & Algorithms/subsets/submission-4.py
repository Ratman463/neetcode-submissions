class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subs(nums: List[int]) -> List[List[int]]:
            if len(nums) == 0:
                return []
            elif len(nums) == 1:
                return [[], [nums[0]]]
            p = subs(nums[1:len(nums)])
            return [*[x for x in p], *[[nums[0], *x] for x in p]]
        return subs(nums)