from COLS import COLS
from ROW import ROW
from utils import *
from config import *
from operator import itemgetter

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
   
    def dist(self, row1, row2, cols = None):
        n,d = 0,0
        for index in cols or self.cols.x:
            n = n + 1
            d = d + cols[index].dist(row1.cells[index], row2.cells[index])**the['p']
        return (d/n)**(1/the['p'])

    def half(self, rows = None, cols = None, above = None):
        def gap(row1,row2): 
            return self.dist(row1,row2,cols)
        def project(row):
            return {'row' : row, 'dist' : cosine(gap(row,A), gap(row,B), c)}
        rows = rows or self.rows
        some = many(rows,the['Half'])
        A    = above if above and the.get('Reuse',0) else any(some)
        def function(r):
            return {'row' : r, 'dist' : gap(r, A)}
        tmp = sorted(list(map(function, some)), key=itemgetter('dist'))
        far = tmp[int(the['Far'] * len(tmp))//1]
        B    = far['row']
        c    = far['dist']
        left, right = [], []
        for n,tmp in enumerate(sorted(list(map(project, rows)), key=itemgetter('dist'))):
            if n < len(rows)//2:
                left.append(tmp['row'])
            else:
                right.append(tmp['row'])
        evals = 1 if the.get('Reuse',0) and above else 2
        return left, right, A, B, c, evals

    def clone(self, init = {}):
        data = DATA([self.cols.names])
        _ = list(map(data.add, init))
        return data


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

