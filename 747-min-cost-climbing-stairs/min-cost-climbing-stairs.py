class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)

        dp = [0] * (N + 1)
        dp[-2] = cost[-1]

        for i in range(N - 2, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])


        store = [-1] * N
        def dfs(s):
            if s >= N:
               return 0

            if store[s] == -1:
                store[s] = cost[s] + min(dfs(s + 1), dfs(s + 2))
            
            return store[s]

        return min(dfs(0), dfs(1))
        