class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * (amount)

        for c in coins:
            for total in range(c, amount+1):
                dp[total] += dp[total-c]
        
        return dp[amount]