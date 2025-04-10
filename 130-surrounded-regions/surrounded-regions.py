class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        neighbors = lambda r, c: [
            (nr, nc) for nr, nc in [
            (r + 1, c), 
            (r, c + 1), 
            (r - 1, c), 
            (r, c - 1)] 
        if 0 <= nr < m and 0 <= nc < n]
        
        checked = set()

        def dfs(r, c, visited):
            neigh = neighbors(r, c)
            surrounded = True

            if len(neigh) != 4:
                surrounded = False

            if surrounded:
                for nr, nc in neigh:
                    if (nr, nc) not in visited and board[nr][nc] == 'O':
                        visited.add((nr, nc))
                        checked.add((nr, nc))

                        s, v = dfs(nr, nc, visited)
                        surrounded &= s
                        if not surrounded: return False, []
            
            return surrounded, visited
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and board[i][j] not in checked:
                    surrounded, cells = dfs(i, j, set([(i, j)]))
                    if surrounded:
                        for ci, cj in cells:
                            board[ci][cj] = 'X'