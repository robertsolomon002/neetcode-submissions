class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        max_ind =0

        total_delta = 0
        curr_tank =0

        for i in range(len(gas)):

            gas_tank = gas[i]
            cost_tank = cost[i]

            delta = gas_tank - cost_tank

            curr_tank += delta
            total_delta += delta

            if curr_tank <0:
                curr_tank =0
                max_ind = i + 1



        if total_delta < 0:
            return -1

        return max_ind
        