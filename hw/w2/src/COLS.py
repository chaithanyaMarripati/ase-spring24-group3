from src.SYM import SYM
from src.NUM import NUM
class COLS:
    def __init__(self, row):
        self.x, self.y, self.all = {}, {}, []
        self.klass = None
        col=None
        for at, txt in enumerate(row.cells):
            col = (NUM if txt[0].isupper() else SYM)()  # Instantiate NUM or SYM directly
            col.txt = txt
            col.at = at
            self.all.append(col)
            if not txt.endswith('X'):
                if txt.endswith('!'):
                    self.klass = col
                if txt.endswith("!") or txt.endswith("+") or txt.endswith("-"):
                    self.y[at]=col
                else:
                    self.x[at]=col
        self.names = row.cells
        

    def add(self, row):
        for cols in [self.x.values(), self.y.values()]:
            for col in cols:
                col.add(row.cells[col.at])
        return row
