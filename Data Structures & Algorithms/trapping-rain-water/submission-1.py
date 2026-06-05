class Solution:
    def trap(self, height: List[int]) -> int:
        # amount[i] = min(left_max_h,right_max_h) - h[i]
        left_mx_dick = deque([])
        right_mx_dick = deque([])

        n = len(height)

        for h in range(n):
            if len(left_mx_dick) > 0 and left_mx_dick[-1] > height[h]:
                left_mx_dick.append(left_mx_dick[-1])
            else:
                left_mx_dick.append(height[h])
            if len(right_mx_dick) > 0 and right_mx_dick[0] > height[n-h-1]:
                right_mx_dick.appendleft(right_mx_dick[0])
            else:
                right_mx_dick.appendleft(height[n-h-1])
        
        # print(left_mx_dick)
        # print(right_mx_dick)

        cnt_rain = 0
        for i in range(len(height)):
            cnt_rain += (min(left_mx_dick[i], right_mx_dick[i]) - height[i])

        return cnt_rain