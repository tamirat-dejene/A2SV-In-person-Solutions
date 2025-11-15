class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.' for _ in range(n)] for _ in range(n)]

        def valid_pos(r, c):
            i, j = r, c

            # check row
            while i >= 0 and board[i][j] != 'Q': i -= 1
            if i >= 0: return False
            i = r

            while i < n and board[i][j] != 'Q': i += 1
            if i < n: return False
            i = r

            # check col
            while j >= 0 and board[i][j] != 'Q': j -= 1
            if j >= 0: return False
            j = c

            while j < n and board[i][j] != 'Q': j += 1
            if j < n: return False
            j = c

            # check main diagonal
            while i >= 0 and j >= 0 and board[i][j] != 'Q': 
                i -= 1
                j -= 1
            if i >= 0 and j >= 0: return False

            i, j = r, c

            while i < n and j < n and board[i][j] != 'Q':
                i += 1
                j += 1
            if i < n and j < n: return False
            i, j = r, c
            
            # check the secondary diagonal
            while i >= 0 and j < n and board[i][j] != 'Q':
                i -= 1
                j += 1
            
            if i >= 0 and j < n: return False
            i, j = r, c

            while i < n and j >= 0 and board[i][j] != 'Q':
                i += 1
                j -= 1
            
            if i < n and j >= 0: return False

            return True

        def bt(q, r):
            if q == 0 or r >= n:
                return q == 0

            ans = 0
            for c in range(n):
                if valid_pos(r, c):
                    board[r][c] = 'Q'
                    ans += bt(q - 1, r + 1)
                    board[r][c] = '.'
            return ans
        
        return bt(n, 0)