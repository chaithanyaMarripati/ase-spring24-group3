from NUM import *
from SYM import *

class COLS:
    def __init__(self, row):
        self.x, self.y, self.all = {}, {}, []
        self.klass = None
        for at, txt in enumerate(row.cells):
            col = NUM(txt, at) if txt[0].isupper() else SYM(txt, at) 
            self.all.append(col)
            if not txt.endswith("X"):
                if txt.endswith("!"):
                    self.klass = col
                if txt.endswith(("!", "+", "-")):
                    self.y[at] = col  
                else:
                    self.x[at] = col
        self.names = row.cells

    def add(self, row):
        for cols in (self.x, self.y):
            for col in cols.values():
                col.add(row.cells[col.at])
        return row

