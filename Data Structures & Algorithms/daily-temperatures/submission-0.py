class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        arr = deque([])
        for i in range(len(temperatures)):
           
            #print(result)
            if len(arr) == 0:
                arr.append(i)
            else:
                top = arr[-1]
                topWeather = temperatures[top]
                while topWeather < temperatures[i] and len(arr) >= 1:
                    top = arr.pop()
                    result[top] = i - top
                    topWeather = temperatures[arr[-1]] if len(arr) > 0 else -1
                arr.append(i)
        return result 