class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets and list of empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)

        def dfs(i):
            # Base case: all empty cells filled
            if i == len(empties):
                return True

            r, c = empties[i]
            b = (r // 3) * 3 + c // 3

            # Try possible digits
            for ch in map(str, range(1, 10)):
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                    # Place the number
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[b].add(ch)

                    # Recurse
                    if dfs(i + 1):
                        return True

                    # Undo (backtrack)
                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[b].remove(ch)

            return False

        dfs(0)
