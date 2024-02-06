import ROW
import COLS
class DATA:
    def __init__(self, src, fun=None):
        self.rows, self.cols = [], None
        self._process_source(src, fun)

    def _process_source(self, src, fun):
        if isinstance(src, str):
            for x in l.csv(src):
                self._add_row(x, fun)
        else:
            for x in src or []:
                self._add_row(x, fun)

    def _add_row(self, t, fun):
        row = t.cells if hasattr(t, 'cells') else ROW.new(t)
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)

    def mid(self, cols=None):
        u = [col.mid() for col in cols or self.cols.all]
        return ROW.new(u)

    def div(self, cols=None):
        u = [col.div() for col in cols or self.cols.all]
        return ROW.new(u)

    def small(self):
        u = [col.small() for col in self.cols.all]
        return ROW.new(u)

    def stats(self, cols=None, fun=None, ndivs=None):
        u = {".N": len(self.rows)}
        for col in self.cols.cols[cols or "y"]:
            u[col.txt] = l.rnd(getattr(col, fun or "mid")(), ndivs)
        return u

    def clone(self, rows=None):
        new = DATA({self.cols.names})
        for row in rows or []:
            new._add_row(row)
        return new
