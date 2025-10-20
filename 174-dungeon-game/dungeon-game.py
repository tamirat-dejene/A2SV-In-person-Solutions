class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])

        dp = [[inf] * (N + 1) for _ in range(M + 1)]

        dp[M][N - 1] = dp[M - 1][N] = 1

        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                need = min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
                dp[r][c] = max(1, need)

        return dp[0][0]



        # min_pow_req, available power
        dp = [[(0, 0)] * N for _ in range(M)]

        for r in range(M):
            for c in range(N):
                gain = dungeon[r][c]
                
                if r == 0 and c == 0:
                    if gain >= 0:
                        dp[0][0] = (1, 1 if gain == 0 else gain)
                    else:
                        dp[0][0] = (abs(gain) + 1, 1)
                    continue
                
                best = (inf, 0)

                # From top
                if r > 0:
                    t_mnp, t_avp = dp[r - 1][c]
                    t_total = t_avp + gain
                    if t_total > 0:
                        candidate = (t_mnp, t_total)
                    else:
                        candidate = (t_mnp + abs(t_total) + 1, 1)
                    best = min(best, candidate)

                # From left
                if c > 0:
                    l_mnp, l_avp = dp[r][c - 1]
                    l_total = l_avp + gain
                    if l_total > 0:
                        candidate = (l_mnp, l_total)
                    else:
                        candidate = (l_mnp + abs(l_total) + 1, 1)
                    best = min(best, candidate)

                dp[r][c] = best
        
        for d in dp:
            print(d)
        return dp[-1][-1][0]
