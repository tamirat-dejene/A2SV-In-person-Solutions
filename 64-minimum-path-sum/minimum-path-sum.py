class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        path_sm = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    path_sm[r][c] = grid[r][c]
                elif r == 0:
                    path_sm[r][c] = grid[r][c] + path_sm[r][c - 1]
                elif c == 0:
                    path_sm[r][c] = grid[r][c] + path_sm[r - 1][c]
                else:
                    path_sm[r][c] = min(path_sm[r][c - 1], path_sm[r - 1][c]) + grid[r][c]
        
        return path_sm[-1][-1]