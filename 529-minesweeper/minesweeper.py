class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])

        def neigh(r, c):
            return [
                (a, b) for a, b in [
                    (r + 1, c), (r, c + 1), (r - 1, c),(r, c - 1),
                    (r + 1, c + 1), (r + 1, c - 1), (r - 1, c - 1), (r - 1, c + 1)
                ] if 0 <= a < m and 0 <= b < n
            ]

        stack = [click]
        
        while stack:
            r, c = stack.pop()

            if board[r][c] == 'M':
                board[r][c] = 'X'
                continue

            if board[r][c] == 'E':
                cnt = 0
                keep = []
                for nr, nc in neigh(r, c):
                    if board[nr][nc] == 'M':
                        cnt += 1
                    if board[nr][nc] == 'E':
                        keep.append((nr, nc))
                
                if cnt == 0:
                    board[r][c] = 'B'
                    for nr, nc in keep:
                        stack.append((nr, nc))
                else:
                    board[r][c] = str(cnt)

        return board


            

        

        