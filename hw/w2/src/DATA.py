from collections import namedtuple
import csv

from SYM import SYM
from NUM import NUM

ROW = namedtuple('ROW', 'cells')

class COLS:
    def __init__(self, row):
        self.x, self.y, self.all, self.klass, self.names = {}, {}, [], None, row.cells
        for at, txt in self.names.items():
            col = (NUM if txt.startswith('A-Z') else SYM)(txt, at)
            self.all.append(col)
            if not txt.endswith('X$'):
                if txt.endswith('!$'):
                    self.klass = col
                (self.y if txt.endswith('!$') else self.x)[at] = col

    def add(self, row):
        for cols in (self.x, self.y):
            for col in cols.values():
                col.add(row.cells[col.at])
        return row

class DATA:
    def __init__(self, src, fun=None):
        self.rows, self.cols = [], None
        if isinstance(src, str):
            with open(src, 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    self.add(row, fun)
        else:
            for x in src or []:
                self.add(x, fun)

    def add(self, t, fun=None):
        row = t.cells if t.cells else ROW(t)
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)

    def mid(self, cols=None):
        u = [col.mid() for col in (cols or self.cols.all)]
        return ROW(u)

    def div(self, cols=None):
        u = [col.div() for col in (cols or self.cols.all)]
        return ROW(u)

    def small(self):
        u = [col.small() for col in self.cols.all]
        return ROW(u)

    def stats(self, cols=None, fun=None, ndivs=None):
        u = {".N": len(self.rows)}
        for col in (self.cols.y if cols is None else [self.cols.names[c] for c in cols]):
            u[col.txt] = round(getattr(col, fun or "mid")(), ndivs) if ndivs else getattr(col, fun or "mid")()
        return u
