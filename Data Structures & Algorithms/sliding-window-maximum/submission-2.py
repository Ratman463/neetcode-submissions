class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()          # 单调递减队列，存下标
        res = []
        for i, x in enumerate(nums):
            # 1. 弹出窗口外的下标
            while q and q[0] <= i - k:
                q.popleft()
            # 2. 弹出队尾小于当前值
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            # 3. 窗口满 k 再输出
            if i >= k - 1:
                res.append(nums[q[0]])
        return res