class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCnt = 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                zeroCnt += 1

        if zeroCnt == 0:
            return [product // x for x in nums]
        elif zeroCnt == 1:
            return [product if x == 0 else 0 for x in nums]
        else:
            return [0]*len(nums)
            
        