class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}
        
    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value
        
    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        exp = formula[1:]
        op1, op2 = exp.split("+")

        def evaluate(op):
            if op.isdigit():
                return int(op)
            return self.sheet.get(op, 0)
        
        return evaluate(op1) + evaluate(op2)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)