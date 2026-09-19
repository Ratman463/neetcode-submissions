class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        max_stack = deque([])
        res = []

        for i in range(len(nums) - k + 1):
            # init:
            if i == 0:
                for j in range(k):
                    new_num = nums[i+j]
                    while len(max_stack) > 0 and new_num > max_stack[-1]:
                        max_stack.pop()
                    max_stack.append(new_num)
                res.append(max_stack[0])
            else:
                old_num = nums[i-1]
                new_num = nums[i+k-1]
                if max_stack[0] == old_num:
                    max_stack.popleft()
                while len(max_stack) > 0 and new_num > max_stack[-1]:
                    max_stack.pop()
                max_stack.append(new_num)
                res.append(max_stack[0])
        return res