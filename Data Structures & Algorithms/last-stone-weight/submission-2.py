class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStones = [-stone for stone in stones]
        heapq.heapify(maxStones)
        while len(maxStones) >= 2:
            # print(maxStones)
            maxStone = heapq.heappop(maxStones)
            nextStone = heapq.heappop(maxStones)
            
            
            if maxStone < nextStone:
                newStone = maxStone - nextStone
                heapq.heappush(maxStones, newStone)
        return -maxStones[0] if len(maxStones) > 0 else 0