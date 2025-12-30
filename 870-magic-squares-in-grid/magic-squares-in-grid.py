class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for r in range(1, m - 1):
            for c in range(1, n - 1):
                seen = set()
                for rr in range(r - 1, r + 2):
                    for cc in range(c - 1, c + 2):
                        if grid[rr][cc] in seen or grid[rr][cc] > 9 or grid[rr][cc] == 0:
                            break
                        seen.add(grid[rr][cc])
                
                if len(seen) != 9:
                    continue

                r1 = grid[r - 1][c - 1] + grid[r - 1][c] + grid[r - 1][c + 1]
                r2 = grid[r][c - 1] + grid[r][c] + grid[r][c + 1]
                r3 = grid[r + 1][c - 1] + grid[r + 1][c] + grid[r + 1][c + 1]

                c1 = grid[r - 1][c - 1] + grid[r][c - 1] + grid[r + 1][c - 1]
                c2 = grid[r - 1][c] + grid[r][c] + grid[r + 1][c]
                c3 = grid[r - 1][c + 1] + grid[r][c + 1] + grid[r + 1][c + 1]

                d1 = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]
                d2 = grid[r - 1][c + 1] + grid[r][c] + grid[r + 1][c - 1]

                ans += (r1 == r2 == r3 == c1 == c2 == c3 == d1 == d2)

        return ans
        