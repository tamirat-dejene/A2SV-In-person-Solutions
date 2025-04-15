class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        neighbor = lambda r, c: [
            (a, b) for a, b in [
                (r + 1, c),
                (r, c + 1),
                (r - 1, c),
                (r, c - 1)
            ] if 0 <= a < m and 0 <= b < n
        ]

        queue = deque()

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        
        while queue:
            r, c, lvl = queue.popleft()
            ans = max(ans, lvl)

            for nr, nc in neighbor(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, lvl + 1))

        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: return -1
        return ans