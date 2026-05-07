class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            # only starts from min
            if num - 1 not in nums_set:
                longest_tmp = 1
                start = num + 1
                while start in nums_set:
                    longest_tmp += 1
                    start += 1
                longest = max(longest, longest_tmp)
        return longest


