class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = sorted(zip(position, speed))
        car = []
        speed = []
        for t in res:
            car.append(t[0])
            speed.append(t[1])
        
        cars = deque(car)
        speeds = deque(speed)

        fleet = 0
        while len(cars) > 0:
            pos = cars[-1]
            lastspeed = speeds[-1]
            delta = target - pos
            elaps = (target - pos) / lastspeed
            while len(cars) > 0 and cars[-1] + elaps*speeds[-1] >= target:
                cars.pop()
                speeds.pop()
            
            fleet += 1

        return fleet