from COLS import COLS
from ROW import ROW
from utils import csv
<<<<<<< HEAD
=======


>>>>>>> 2ec04a716ad72c88cce8920bf6f9e04a8b963931
class DATA:
    def __init__(self, src):
        self.rows, self.cols = [], None
<<<<<<< HEAD
        if isinstance(src,str) == False:
            raise Exception("Data source should be a string")
        csv(src,self.add)

    def add(self, r, fun=None):
        row =r if 'cells' in r else ROW(r)
=======
        if isinstance(src, str):
            csv(src, self.add)
        else:
            self.add(src, fun)

    def add(self, r, fun=None):
        row = r if isinstance(r, ROW) and r.cells else ROW(r)
>>>>>>> 2ec04a716ad72c88cce8920bf6f9e04a8b963931
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
<<<<<<< HEAD
        for col in (self.cols.y if cols is None else [self.cols.names[c] for c in cols]):
            current_col= self.cols.all[col]
            u[current_col.txt] = round(getattr(current_col, fun or "mid")(), ndivs) if ndivs else getattr(current_col, fun or "mid")()
        return u
=======
        for col in self.cols.y if cols is None else [self.cols.names[c] for c in cols]:
            current_col = self.cols.all[col]
            u[current_col.txt] = (
                round(getattr(current_col, fun or "mid")(), ndivs)
                if ndivs
                else getattr(current_col, fun or "mid")()
            )
        return u
>>>>>>> 2ec04a716ad72c88cce8920bf6f9e04a8b963931
