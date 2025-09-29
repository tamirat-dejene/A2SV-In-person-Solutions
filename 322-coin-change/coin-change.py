class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf for _ in range(amount)]

        for amount in range(1, amount + 1):
            for coin in coins:
                if amount >= coin:
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])
        
        return dp[amount] if dp[amount] != inf else -1
        
        