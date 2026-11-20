class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - position[i]) / speed[i] for i in range(len(position))]
        position_to_time = {position[i]: time[i] for i in range(len(position))}
        position = sorted(position)[::-1]
        fleets = 0
        prev_fleet_arrival = -float('inf')
        print(position)
        for i in range(len(position)):
            trafficless_arrival_time = position_to_time[position[i]]
            if trafficless_arrival_time <= prev_fleet_arrival:
                continue
            else:
                fleets += 1
                prev_fleet_arrival = trafficless_arrival_time
        return fleets
