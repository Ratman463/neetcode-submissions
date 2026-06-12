class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # binsearch k
        def canEatingUpWithK(piles: List[int], h: int, k: int) -> bool:
            total_h = sum([math.ceil(pile / k) for pile in piles])
            print([h,mid,total_h])
            return total_h <= h

        left, right = 1, max(piles) + 1
        mid = (left + right) // 2
        best = right

        while left < right:
            mid = (left + right) // 2
            if canEatingUpWithK(piles, h, mid):
                right = mid
                best = min(best, mid)
            else:
                left = mid + 1
        return best