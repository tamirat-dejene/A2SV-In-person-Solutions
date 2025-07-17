class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        root = [[(r, c) for c in range(n)] for r in range(n)]
        size = [[1 for _ in range(n)] for _ in range(n)]

        def valid(r, c):
            return [
                (a, b) for a, b in [
                    (r + 1, c),
                    (r, c + 1),
                    (r - 1, c),
                    (r, c - 1)
                ] if 0 <= a < n and 0 <= b < n
            ]

        def find(r, c):
            if root[r][c] != (r, c):
                root[r][c] = find(*root[r][c])

            return root[r][c]

        def union(r1, c1, r2, c2):
            pr1, pc1 = find(r1, c1)
            pr2, pc2 = find(r2, c2)

            if pr1 == pr2 and pc1 == pc2:
                return False
            
            if size[pr1][pc1] < size[pr2][pc2]:
                pr1, pc1, pr2, pc2 = pr2, pc2, pr1, pc1

            root[pr2][pc2] = (pr1, pc1)
            size[pr1][pc1] += size[pr2][pc2]

            return True
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0: 
                    continue

                for nr, nc in valid(r, c):
                    if grid[nr][nc] == 1:
                        union(r, c, nr, nc)

        ans = 0
        
        for r in range(n):
            for c in range(n):
                pr, pc = find(r, c)

                if grid[r][c] == 1:
                    ans = max(ans, size[pr][pc])                 
                else:
                    sm = size[pr][pc]
                    pars = set((pr, pc))

                    for nr, nc in valid(r, c):
                        if grid[nr][nc] == 0: 
                            continue

                        npr, npc = find(nr, nc)

                        if (npr, npc) in pars:
                            continue

                        sm += size[npr][npc]
                        pars.add((npr, npc))
                    
                    ans = max(ans, sm)
        
        return ans
        