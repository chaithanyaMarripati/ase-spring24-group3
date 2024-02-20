class COLS:
    def __init__(self, row):
        self.x, self.y, self.all = [], [], []
        klass, col = None, None

        for at, txt in row.cells.items():
            col = NUM(txt, at) if txt.startswith("^[A-Z]") else SYM(txt, at)
            self.all.append(col)

            if not txt.endswith("X$"):
                if txt.endswith("!$"):
                    klass = col
                (self.y if txt.endswith("[!+-]$") else self.x)[at] = col

        self.klass = klass
        self.names = row.cells

    def add(self, row):
        for cols in [self.x, self.y]:
            for col in cols:
                col.add(row.cells[col.at])

        return row
