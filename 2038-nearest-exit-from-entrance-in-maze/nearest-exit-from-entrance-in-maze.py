class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        neighbor = lambda r, c: [
            (a, b) for a, b in [
                (r, c + 1),
                (r + 1, c),
                (r, c - 1),
                (r - 1, c)
            ] if 0 <= a < m and 0 <= b < n
        ]

        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set()

        while queue:
            r, c, d = queue.popleft()
            if (r, c) in visited: continue
            visited.add((r, c))
            neigh = neighbor(r, c)
            maze[r][c] = '+'
            
            for nr, nc in neigh:
                if maze[nr][nc] == '.':
                    if len(neighbor(nr, nc)) != 4: return d + 1
                    queue.append((nr, nc, d + 1))
        
        return -1