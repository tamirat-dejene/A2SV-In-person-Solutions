class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        queue = deque([(0, 0, 0,  k)]) # row, col, cost, k
        vis = [[-1] * n for _ in range(m)]

        while queue:
            r, c, cost, k = queue.popleft()
            if r == m - 1 and c == n - 1:
                return cost
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                nk = k

                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 1:
                        nk -= 1
                        if nk < 0:
                            continue
                    if nk > vis[nr][nc]:
                        vis[nr][nc] = nk
                        queue.append((nr, nc, cost + 1, nk))
        
        return -1