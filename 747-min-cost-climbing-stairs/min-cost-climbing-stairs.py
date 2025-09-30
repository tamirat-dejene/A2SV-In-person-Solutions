class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)


        store = [-1] * N
        def dfs(s):
            if s >= N:
               return 0

            if store[s] == -1:
                store[s] = cost[s] + min(dfs(s + 1), dfs(s + 2))
            
            return store[s]

        return min(dfs(0), dfs(1))
        