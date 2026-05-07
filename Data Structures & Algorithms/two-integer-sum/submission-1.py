class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums: List[int] = sorted(nums)
        dict_ans: Dict[int,int] = {}
        for i in range(len(nums)):
            dict_ans[target - nums[i]] = i
        
        for i in range(len(nums)):
            if(dict_ans.get(nums[i], 'N/A') != 'N/A'):
                t = dict_ans.get(nums[i], 'N/A')
                if(t != i):
                    return [i, dict_ans.get(nums[i], 0)]
        return [0, 0]