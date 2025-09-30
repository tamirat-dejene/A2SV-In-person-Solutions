class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        # Bottom Up
        dp = [0] * N

        for b in range(N - 2, -1, -1):
            for s in range(b + 1, N):
                dp[b] = max(dp[b], prices[s] - prices[b] + (dp[s + 2] if s + 2 < N else 0))
            
            if b + 1 < N:
                dp[b] = max(dp[b], dp[b + 1])
        
        return dp[0]


        # Top down
        
        profit = [-1] * N
        def dfs(b):
            if b >= N:
                return 0
            
            if profit[b] == -1:
                profit[b] = 0
                for s in range(b + 1, N):
                    profit[b] = max(profit[b], prices[s] - prices[b] + dfs(s + 2))

                profit[b] = max(profit[b], dfs(b + 1))
            
            return profit[b]
        
        return dfs(0)