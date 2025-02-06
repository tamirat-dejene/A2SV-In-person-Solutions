class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_grid(si, sj):
            seen = set()
            for i in range(si, si + 3):
                for j in range(sj, sj + 3):
                    if board[i][j] != ".":
                        if board[i][j] in seen: return False
                        seen.add(board[i][j])
            return True
        
    
        def check_row(row):
            seen = set()
            for i in range(9):
                if row[i] != ".":
                    if row[i] in seen: return False
                    seen.add(row[i])
            return True
        
        def check_col(col_num):
            seen = set()
            for row in board:
                if row[col_num] != '.':
                    if row[col_num] in seen: return False
                    seen.add(row[col_num])
            return True
        
        for row in board: 
            if not check_row(row): return False
        
        for i in range(9):
            if not check_col(i): return False
        

        if not (check_grid(0, 0) and check_grid(0, 3) and check_grid(0, 6) and check_grid(3, 0) and check_grid(3, 3) and check_grid(3, 6) and check_grid(6, 0) and check_grid(6, 3) and check_grid(6, 6)): return False
        return True

        


        