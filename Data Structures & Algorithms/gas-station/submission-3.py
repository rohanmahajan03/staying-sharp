class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        cum_sum = 0
        start = 0
        for i in range(len(gas)):
            cum_sum += gas[i] - cost[i]
            if cum_sum < 0:
                start = i + 1
                cum_sum = 0
        return start


