class Solution:
    def trap(self, height: List[int]) -> int:
        # amount[i] = min(left_max_h,right_max_h) - h[i]
        if len(height) <= 2:
            return 0

        l_breast, r_breast = 0, 1
        cnt_rain = 0

        n = len(height)

        while r_breast <= n:
            if r_breast < n and height[r_breast] >= height[l_breast]:
                for j in range(l_breast, r_breast+1):
                    cnt_rain += max(0, (height[l_breast] - height[j]))
                l_breast = r_breast
                r_breast += 1

            elif r_breast < n and height[r_breast] < height[l_breast]:

                r_breast += 1
            else:
                # left max = height[l_breast]
                # right max = rmax[i]
                tmp_rmax = 0
                for i in range(n-1, l_breast, -1):
                    if(height[i] > tmp_rmax):
                        tmp_rmax = height[i]
                    cnt_rain += (tmp_rmax - height[i])
                r_breast += 1

        return cnt_rain