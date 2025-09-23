class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    ways[r][c] = 1
                else:
                    ways[r][c] = ways[r - 1][c] + ways[r][c - 1]
        
        return ways[m-1][n-1]
        