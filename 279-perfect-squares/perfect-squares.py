class Solution:
    def numSquares(self, n: int) -> int:
        if sqrt(n) == int(sqrt(n)): return 1

        perfect = [i for i in range(1, n + 1) if sqrt(i) == int(sqrt(i))]
        dp = [1 if sqrt(i) == int(sqrt(i)) else i for i in range(n + 1)]

        for num in range(1, n + 1):
            for i in range(len(perfect)):
                if num < perfect[i]:
                    break

                dp[num] = min(dp[num], 1 + dp[num - perfect[i]])

        return dp[n]























