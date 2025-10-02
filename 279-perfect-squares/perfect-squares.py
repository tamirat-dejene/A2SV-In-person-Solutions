class Solution:
    def __init__(self):
        self.perfect = [i for i in range(1, 10001) if sqrt(i) == int(sqrt(i))]
        self.dp = [1 if sqrt(i) == int(sqrt(i)) else i for i in range(10001)]

    def numSquares(self, n: int) -> int:
        if sqrt(n) == int(sqrt(n)): return 1

        for num in range(1, n + 1):
            for i in range(len(self.perfect)):
                if num < self.perfect[i]:
                    break

                self.dp[num] = min(self.dp[num], 1 + self.dp[num - self.perfect[i]])

        return self.dp[n]























