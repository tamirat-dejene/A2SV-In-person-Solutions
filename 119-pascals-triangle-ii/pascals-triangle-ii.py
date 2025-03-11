class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def get_pascal(start, row):
            if row == 0: return start
            next_row = [1]
            for i in range(1, len(start)):
                next_row.append(start[i] + start[i - 1])
            next_row.append(1)

            return get_pascal(next_row, row - 1)
        
        return get_pascal([1], rowIndex)


        