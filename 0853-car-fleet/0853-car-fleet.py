class Solution(object):
    def carFleet(self, target, position, speed):
        cars = []

        for i in range(len(position)):
            distance = target - position[i]
            cars.append((position[i], distance, speed[i]))

        cars.sort(reverse=True)

        fleets = 0
        slowest_distance = 0
        slowest_speed = 1

        for pos, distance, car_speed in cars:
            # distance / car_speed > slowest_distance / slowest_speed
            if distance * slowest_speed > slowest_distance * car_speed:
                fleets += 1
                slowest_distance = distance
                slowest_speed = car_speed

        return fleets