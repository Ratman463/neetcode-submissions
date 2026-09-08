class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dick = {}
        new_dick = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = x**2 + y**2
            if dick.get(dist) is None:
                new_dick.append(dist)
            dick.setdefault(dist, []).append([x, y])
        

        heapq.heapify(new_dick)

        res = []

        while len(res) < k:
            distance = heapq.heappop(new_dick)
            dicks = dick.get(distance, [])

            res = [*res, *dicks]



        return res
