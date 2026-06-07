from collections import deque
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        if n < 2:
            return 0

        max_w = 0
        l_dicks = 0
        r_dicks = n - 1

        while r_dicks > l_dicks:
            # shirnk:
            # f(m,n) -> f(m+1,n) or f(m, n-1)
            # ensure f(m,n) = h(m)*(n-m) > f(m, [n-1, n-2, n-3, ... ,m+1])
            # or f(m,n) = h(n)*(n-m) > f([m+1,m+2, ... n-1], n)
            # if f(n) < f(m), f(m,n) = h(n) * (n-m), move n else move m
            tmp_w = (r_dicks - l_dicks) * min(heights[r_dicks], heights[l_dicks])

            if tmp_w > max_w:
                max_w = tmp_w
            
            if heights[l_dicks] < heights[r_dicks]:
                l_dicks += 1
            else:
                r_dicks -= 1
        return max_w