from COLS import COLS
from ROW import ROW
from utils import csv
from config import *

class DATA:
    def __init__(self, src, fun=None):
        self.rows, self.cols = [], None
        if isinstance(src, str):
            csv(src, self.add)
        else:
            self.add(src, fun)

    def add(self, r, fun=None):
        row = r if isinstance(r, ROW) and r.cells else ROW(r)
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
        for col in self.cols.y if cols is None else [self.cols.names[c] for c in cols]:
            current_col = self.cols.all[col]
            u[current_col.txt] = (
                round(getattr(current_col, fun or "mid")(), ndivs)
                if ndivs
                else getattr(current_col, fun or "mid")()
            )
        return u


    def farapart(self, data, a=None, sortp=False):
            rows = data.rows or self.rows
            far = int(len(rows) * the.get("Far", 0.95))
            evals = 1 if a else 2
            a = a or any(rows).neighbors(self, rows)[far]
            b = a.neighbors(self, rows)[far]
            if sortp and b.d2h(self) < a.d2h(self):
                a,b=b,a
            return a, b, a.dist(b,self)

    def cluster(self, rows = None , min = None, cols = None, above = None):
        rows = rows or self.rows
        min  = min or len(rows)**the['min']
        cols = cols or self.cols.x
        node = { 'data' : self.clone(rows) }
        if len(rows) >= 2*min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows,cols,above)
            node['left']  = self.cluster(left,  min, cols, node['A'])
            node['right'] = self.cluster(right, min, cols, node['B'])
        return node

