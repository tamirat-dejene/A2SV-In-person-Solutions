class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        grd = [[0]*3*n for _ in range(3*n)]

        for r in range(n):
            for c in range(n):
                b = grid[r][c]
                if b == '/':
                    grd[3*r][3*c + 2] = 1
                    grd[3*r + 1][3*c + 1] = 1
                    grd[3*r + 2][3*c] = 1
                elif b != ' ':
                    grd[3*r][3*c] = 1
                    grd[3*r + 1][3*c + 1] = 1
                    grd[3*r + 2][3*c + 2] = 1

        def neigh(r, c):
            return [
                (a, b) for a, b in [
                    (r + 1, c),
                    (r, c + 1),
                    (r - 1, c),
                    (r, c - 1)
                ] if 0 <= a < 3*n and 0 <= b < 3*n
            ]

        print(grd)

        def dfs(r, c):
            for nr, nc in neigh(r, c):
                if grd[nr][nc] == 0:
                    grd[nr][nc] = 1
                    dfs(nr, nc)
        cnt = 0
        for r in range(3*n):
            for c in range(3*n):
                if grd[r][c] == 0:
                    grd[r][c] = 1
                    dfs(r, c)
                    cnt += 1
        
        return cnt

            
        
        