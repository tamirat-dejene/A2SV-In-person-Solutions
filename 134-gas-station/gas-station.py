class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N, start, tank = len(gas), 0, 0

        for i in range(2 * N):
            tank += gas[i % N] - cost[i % N]

            if tank < 0:
                start = (i + 1) % N
                tank = 0
            
            elif (i + 1) % N == start:
                return start

        return -1        