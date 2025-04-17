class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        neighbor = lambda r, c: [
            (a, b) for a, b in [
                (r, c + 1),
                (r + 1, c),
                (r, c - 1),
                (r - 1, c)
            ] if 0 <= a < m and 0 <= b < n
        ]
        
        queue = deque()
        visited = set()
        for r in range(m):
            found = False
            for c in range(n):
                if grid[r][c] == 1:
                    found = True
                    visited.add((r, c))
                    queue.append((r, c))
                    break
            if found: break
        
        p = 0
        while queue:
            r, c = queue.pop()
            neigh = neighbor(r, c)

            p += 4 - len(neigh)
            

            for nr, nc in neighbor(r, c):
                if grid[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                elif grid[nr][nc] == 0:
                    p += 1
        
        return p

        