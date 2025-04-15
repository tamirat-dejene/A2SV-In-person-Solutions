class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
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
            for c in range(n):
                if isWater[r][c] == 1:
                    queue.append((r, c, 0))
                    visited.add((r, c))
                    isWater[r][c] = 0
        

        while queue:
            r, c, lvl = queue.popleft()
            isWater[r][c] = lvl

            for nr, nc in neighbor(r, c):
                if isWater[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, lvl + 1))
        
        return isWater

            




        