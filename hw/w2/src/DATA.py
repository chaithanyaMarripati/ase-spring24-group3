from src.COLS import COLS
from src.ROW import ROW
from src.utils import csv
class DATA:
    def __init__(self, src):
        self.rows, self.cols = [], None
        if isinstance(src,str) == False:
            raise Exception("Data source should be a string")
        csv(src,self.add)

    def add(self, r, fun=None):
        row =r if 'cells' in r else ROW(r)
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
            current_col= self.cols.all[col]
            u[current_col.txt] = round(getattr(current_col, fun or "mid")(), ndivs) if ndivs else getattr(current_col, fun or "mid")()
        return u
