from COLS import COLS
from ROW import ROW
from utils import *
from config import *
from operator import itemgetter
from node_module import NODE
import config

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

    def clone(self, init = {}):
        data = DATA([self.cols.names])
        _ = list(map(data.add, init))
        return data


    def farapart(self, data, a=None, sortp=False):
            if isinstance(data,list):
                rows = data
            else:
                rows = data.rows or self.rows
            far = int(len(rows) * the.get("Far", 0.95))
            evals = 1 if a else 2
            a = a or any(rows).neighbors(self, rows)[far]
            b = a.neighbors(self, rows)[far]
            if sortp and b.d2h(self) < a.d2h(self):
                a,b=b,a
            return a, b, a.dist(b,self),evals

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
    
    def half(self, rows, sortp = False, before = None, evals = None):
        evals = evals or 0
        some = many(rows, min(the['Half'], len(rows)))
        a, b, C, evals = self.farapart(some, before, sortp)

        def d(row1, row2):
            return row1.dist(row2, self)

        def project(r):
            return (d(r, a)**2 + C**2 - d(r, b)**2) / (2 * C)

        sorted_rows = sorted(rows, key=project)
        
        mid_index = len(sorted_rows) // 2
        as_ = sorted_rows[:mid_index]
        bs = sorted_rows[mid_index:]

        return as_, bs, a, b, C, d(a, bs[0]), evals
    
    def tree(self, sortp = False):
        evals = 0
        def _tree(data, above=None, lefts=None, rights=None, node=None):
            nonlocal evals
            node = NODE(data)

            if len(data.rows) > 2 * (len(self.rows) ** 0.5):
                lefts, rights, node.left, node.right, node.C, node.cut, evals1 = self.half(data.rows, sortp, above)
                evals += evals1
                node.lefts = _tree(self.clone(lefts), node.left)
                node.rights = _tree(self.clone(rights), node.right)

            return node

        return _tree(self), evals
    
    def branch(self, stop=None):
        evals, rest = 1, []
        stop = stop or (2 * (len(self.rows) ** 0.5))

        def _branch(data, above=None, left=None, lefts=None, rights=None):
            nonlocal evals, rest
            if len(data.rows) > stop:
                lefts, rights, left, _, _, _, _ = self.half(data.rows, True, above)
                evals += 1
                rest.extend(rights)
                return _branch(self.clone(lefts), left)
            else:
                return self.clone(data.rows), self.clone(rest), evals

        return _branch(self)


