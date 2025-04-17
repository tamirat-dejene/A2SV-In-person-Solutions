class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
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

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c, 0))
        
        dis = -1
        if len(queue) == m * n: return dis
        
        while queue:
            r, c, d = queue.popleft()
            dis = d

            for nr, nc in neighbor(r, c):
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, d + 1))
        
        return dis