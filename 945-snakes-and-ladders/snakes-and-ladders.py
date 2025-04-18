class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def nxt(r, c):
            fwd = (r % 2 == 1) if n % 2 == 0 else (r % 2 == 0)
            if (fwd and c < n - 1) or (not fwd and c > 0):
                return (r, c + (1 if fwd else -1))
            return (r - 1, c) if r - 1 >= 0 else (-1, -1)
        
        def pos(val):
            r = n - ceil(val / n)
            if (n % 2 == 0 and r % 2 == 1) or (n % 2 == 1 and r % 2 == 0):
                return (r, val - (n - r - 1) * n - 1)
            else:
                return (r, (n - r) * n - val)
        
        queue = deque([(n - 1, 0, 0)])
        visited = set([(n - 1, 0)])

        while queue:
            r, c, d = queue.popleft()

            if (n % 2 == 0 and (r, c) == (0, 0)) or (n % 2 == 1 and (r, c) == (0, n - 1)): return d

            for _ in range(6):
                nr, nc = nxt(r, c)

                if 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] != -1:
                        nr, nc = pos(board[nr][nc])
                    
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, d + 1))
                
                r, c = nxt(r, c)

        return -1


        