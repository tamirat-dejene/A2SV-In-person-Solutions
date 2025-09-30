class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        profit = [-1] * N
        
        def dfs(b):
            if b >= N:
                return 0
            
            if profit[b] == -1:
                p = 0
                for s in range(b + 1, N):
                    p = max(p, prices[s] - prices[b] + dfs(s + 2))

                profit[b] = max(p, dfs(b + 1))
            
            return profit[b]
        
        return dfs(0)