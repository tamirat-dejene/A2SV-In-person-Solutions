class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        neighbor = lambda r, c: [
            (nr, nc) for nr, nc in [
            (r + 1, c), 
            (r, c + 1), 
            (r - 1, c), 
            (r, c - 1)] 
        if 0 <= nr < m and 0 <= nc < n]

        visited = [[False] * n for _ in range(m)]
        
        def dfs(sr, sc, r, c, ch):
            if visited[r][c]: return True
            visited[r][c] = True
            
            for nr, nc in neighbor(r, c):
                if grid[nr][nc] == ch:
                    if (nr, nc) == (sr, sc): 
                        continue   
                    if dfs(r, c, nr, nc, ch): return True

            return False
        
        for r in range(m):
            for c in range(n):
                if not visited[r][c] and dfs(-1, -1, r, c, grid[r][c]): 
                    return True

        return False