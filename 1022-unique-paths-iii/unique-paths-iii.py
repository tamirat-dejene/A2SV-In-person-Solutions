class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start, end, intrm = (), (), []
        path = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    end = (r, c)
                elif grid[r][c] == 0:
                    intrm.append((r, c))
        path[start[0]][start[1]] = 1

        def neigh(r, c):
            nh = []
            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1 and path[nr][nc] == 0: 
                    nh.append((nr, nc))
            return nh

        def dfs(r, c):
            if (r, c) == end:
                return not any(path[rr][cc] == 0 for rr, cc in intrm)
            
            cnt = 0
            for nr, nc in neigh(r, c):
                path[nr][nc] = 1
                cnt += dfs(nr, nc)
                path[nr][nc] = 0
            
            return cnt
        
        return dfs(*start)
        