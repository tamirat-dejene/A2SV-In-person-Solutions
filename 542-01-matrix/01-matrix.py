class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
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
                if mat[r][c] == 0: 
                    queue.append((r, c, 0))
                    visited.add((r, c))

        while queue:
            r, c, d = queue.popleft()
            mat[r][c] = d

            for nr, nc in neighbor(r, c):
                if mat[nr][nc] != 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, d + 1))

        return mat            