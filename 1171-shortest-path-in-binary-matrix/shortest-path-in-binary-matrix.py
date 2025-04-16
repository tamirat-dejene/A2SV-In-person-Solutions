class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        neighbor = lambda r, c: [
            (a, b) for a, b in [
                (r, c + 1),
                (r + 1, c),
                (r, c - 1),
                (r - 1, c),
                (r + 1, c + 1),
                (r + 1, c - 1),
                (r - 1, c + 1),
                (r - 1, c - 1)
            ] if 0 <= a < n and 0 <= b < n
        ]

        if grid[0][0] == 1: return -1
        queue = deque([(0, 0, 1)])
        visited = set()

        while queue:
            r, c, lvl = queue.popleft()
            if (r, c) in visited: continue
            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return lvl
            grid[r][c] = 1

            for nr, nc in neighbor(r, c):
                if grid[nr][nc] == 0:
                    queue.append((nr, nc, lvl + 1))
        
        return -1
