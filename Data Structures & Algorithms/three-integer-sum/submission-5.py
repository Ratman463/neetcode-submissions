class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def numToStr(num: int) -> str:
            if num > 0:
                return '+' + str(num)
            else:
                return '-' + str(abs(num))

        nums = sorted(nums)
        res = []
        resHash: dict[str, bool] = {}
        print(nums)

        for i in range(len(nums) - 2):
            [j, k] = [i + 1, len(nums) - 1]

            while j < k:
                # nums[j] + nums[k] = -nums[i]
                while nums[j] + nums[k] < -nums[i] and j < k:
                    j += 1
                while nums[j] + nums[k] > -nums[i] and j < k:
                    k -= 1
                # print([i,j,k])
                if nums[j] + nums[k] == -nums[i] and j < k:
                    hash = numToStr(nums[i]) + numToStr(nums[j]) + numToStr(nums[k])
                    if not resHash.get(hash):
                        resHash[hash] = True
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
        return res