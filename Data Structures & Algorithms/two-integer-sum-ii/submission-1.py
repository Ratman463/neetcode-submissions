class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        [i, j] = [0, len(numbers) - 1]
        while j > i:
            tsum = numbers[i] + numbers[j]
            if tsum == target:
                return [i + 1, j + 1]
            elif tsum < target:
                i += 1
            else:
                j -= 1


        return [i + 1, j + 1]