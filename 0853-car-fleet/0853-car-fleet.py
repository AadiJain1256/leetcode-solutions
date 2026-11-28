class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        fleet=0
        slowest_time_ahead=0

        for pos,vel in cars:
            time=(target-pos)/vel
            if time > slowest_time_ahead:
                fleet+=1
                slowest_time_ahead=time

        return fleet