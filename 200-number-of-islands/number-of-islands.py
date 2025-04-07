class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        m, n = len(grid), len(grid[0])
        

        def dfs(r, c):
            if grid[r][c] == '0': return

            grid[r][c] = '0'

            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                
                if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == '1':
                    dfs(nr, nc)

        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)  

        return cnt
                
        