class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # (m, n)
        count = []

        for s in strs:
            count.append((s.count('0'), s.count('1')))

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for mi, ni in count:

            for i in range(m, mi - 1, -1):
                for j in range(n, ni - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - mi][j - ni] + 1)
        
        return dp[m][n]