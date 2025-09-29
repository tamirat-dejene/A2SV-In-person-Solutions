class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        store = [[-1] * (amount + 1) for _ in range(len(coins))]

        def dfs(amount, i):
            if amount == 0:
                return 1
            elif amount < 0 or i >= len(coins):
                return 0

            if store[i][amount] == -1:
                store[i][amount] = dfs(amount -  coins[i], i) + dfs(amount, i + 1)

            return store[i][amount]
        
        return dfs(amount, 0)
        