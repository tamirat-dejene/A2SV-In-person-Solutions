class UF:
    def __init__(self, m, n):
        self.root = [[(r, c) for c in range(n)] for r in range(m)]
        self.size = [[1] * n for _ in range(m)]

    def find(self, r, c):
        if (r, c) != self.root[r][c]:
            pr, pc = self.root[r][c]
            self.root[r][c] = self.find(pr, pc)
        return self.root[r][c]


    def union(self, r1, c1, r2, c2):
        pr1, pc1 = self.find(r1, c1)
        pr2, pc2 = self.find(r2, c2)

        if (pr1, pc1) == (pr2, pc2): return False

        if self.size[pr1][pc1] >= self.size[pr2][pc2]:
            self.root[pr2][pc2] = (pr1, pc1)
            self.size[pr1][pc1] += self.size[pr2][pc2]
        else:
            self.root[pr1][pc1] = (pr2, pc2)
            self.size[pr2][pc2] += self.size[pr1][pc1]
        
        return True

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        valid = lambda r, c: 0 <= r < m and 0 <= c < n

        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(-1, 0), (0, 1)]
        }

        uf = UF(m, n)

        for r in range(m):
            for c in range(n):
                
                for dr, dc in dirs[grid[r][c]]:
                    nr, nc = r + dr, c + dc
                    
                    # Can I move to the neighbor cell and be back?
                    if valid(nr, nc) and (-dr, -dc) in dirs[grid[nr][nc]]:
                        uf.union(r, c, nr, nc)

        return uf.find(0, 0) == uf.find(m - 1, n - 1)

        