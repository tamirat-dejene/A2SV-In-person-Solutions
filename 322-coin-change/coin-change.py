class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] + [inf for _ in range(amount)]

        for amount in range(1, amount + 1):
            for coin in coins:
                if coin > amount:
                    break
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])
        
        return dp[amount] if dp[amount] != inf else -1
        
        