class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        n = len(heights)
        left = [0] * n
        right = [0] * n
        
        # [7 1 7 2 2 4]
        # [0] -> [1] -> [1 2] -> [1 3] -> [1 3 4] -> [1 3 4 5]   
        stack = deque([])
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        for j in range(n-1, -1, -1):
            while stack and heights[stack[0]] >= heights[j]:
                stack.popleft()
            right[j] = stack[0] if stack else n
            stack.appendleft(j)
                
        for i in range(n):
            largest = max(largest, heights[i] * (right[i] - left[i] - 1))
        
        return largest