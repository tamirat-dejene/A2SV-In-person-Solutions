class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for r in range(k - 1, m):
            for c in range(k - 1, n):
                
                # sub-matrix
                store = set()
                for rr in range(r - k + 1, r + 1):
                    for cc in range(c - k + 1, c + 1):
                        store.add(grid[rr][cc])
                srted = sorted(store)
            
                ans[r - k + 1][c - k + 1] = 0 if len(srted) <= 1 else min(abs(srted[i] - srted[i - 1]) for i in range(1, len(srted)))
        
        return ans