from NUM import NUM
from SYM import SYM

class COLS:
    def __init__(self, row):
        self.x, self.y, self.all = {}, {}, {}
        self.klass = None
        for at, txt in enumerate(row):
            col = NUM(txt, at) if txt[0].isupper() else SYM(txt, at)
            self.all[at] = col
            if "!" in txt:
                self.klass = col
            if "+" in txt or "-" in txt or "!" in txt:
                self.y[at] = col
            else:
                self.x[at] = col
    def add(self, row):
        for col in self.all.values():
            col.add(row[col.at])
        return row