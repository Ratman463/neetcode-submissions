class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d: Dict[int, int] = {}
        for num in nums:
            if not d.get(num):
                d[num] = 1
            else:
                d[num] += 1
        
        heap = []
        for key in d:
            value = d.get(key)
            heapq.heappush(heap, value)
            if len(heap) > k:
                heapq.heappop(heap)

        cutoff = heap[0] if len(heap) > 0 else 0

        res = []
        for key in d:
            val = d[key]
            if val:
                if val >= cutoff:
                    res.append(key)
        return res