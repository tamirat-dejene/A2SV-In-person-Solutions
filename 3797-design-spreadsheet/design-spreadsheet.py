class Spreadsheet:
    def __init__(self, rows: int):
        self.sheet = [defaultdict(int) for _ in range(26)]

    def setCell(self, cell: str, value: int) -> None:
        col, row = self.get_cr(cell)
        self.sheet[col][row] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        l, r = formula[1:].split('+') 
        return self.resolve(l) + self.resolve(r)
    
    def get_cr(self, cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])
        return col, row
    
    def resolve(self, val):
        try:
            return int(val)
        except:
            col, row = self.get_cr(val)
            return self.sheet[col][row]
        
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)