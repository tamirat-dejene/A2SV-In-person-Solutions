class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]

        for r in range(1, query_row + 1):
            rw = [max(0, (row[0] - 1) / 2)]
            for c in range(1, len(row)):
                rw.append(
                    max(0, (row[c] - 1) / 2) + max(0, (row[c - 1] - 1) / 2)
                )
            rw.append(max(0, (row[-1] - 1) / 2))
            row = rw
            
        
        return row[query_glass] if row[query_glass] < 1 else 1
                        








        