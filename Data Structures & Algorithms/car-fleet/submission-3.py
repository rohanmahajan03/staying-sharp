class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # for each car, figure out how long they will take to get to the finish
        # (target - position) / speed
        # if anyone in front of them is taking longer, they will become a fleet with that person.
        # 3, 4.5, 10, 3
        time = {}
        for i in range(len(position)):
            time[position[i]] = (target - position[i]) / speed[i]
        descending_positions = sorted(position)[::-1]
        fleets = 0
        last_reached_time = -float("inf")
        # print("time: ", time)
        # print("descending positions: ", descending_positions)
        for pos in descending_positions:
            if time[pos] > last_reached_time:
                fleets += 1
                last_reached_time = time[pos]
        return fleets
        


        
        