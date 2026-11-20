class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diffs) < 0:
            return -1
        cum_sum = 0
        start = 0
        for i in range(len(diffs)):
            cum_sum += diffs[i]
            if cum_sum < 0:
                start = i + 1
                cum_sum = 0
        return start


