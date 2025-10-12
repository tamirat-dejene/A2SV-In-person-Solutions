class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        N = len(power)
        count = Counter(power)

        dp = [0] * (N + 1)
        idx = dict()

        for i in range(N - 1, -1, -1):
            nxt = power[i] + 3
            
            if nxt not in idx:
                idx[nxt] = min(N, bisect_left(power, nxt))

            dp[i] = max(power[i] * count[power[i]] + dp[idx[nxt]], dp[i + 1])

        return dp[0]