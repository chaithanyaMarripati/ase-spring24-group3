class ROW:
    def __init__(self, t):
        self.cells = t

    def d2h(self, data):
        d, n, p = 0, 0, 2

        for col in data.cols.y:
            x = self.cells.get(col.at)
            if x is None:
                print("?", end='', file=sys.stderr)
            else:
                n += 1
                d += abs(col.heaven - col.norm(x)) ** p

        return (d / n) ** (1 / p)

    def dist(self, other, data):
        d, n, p = 0, 0, the.p

        for col in data.cols.x:
            n += 1
            d += col.dist(self.cells.get(col.at), other.cells.get(col.at)) ** p

        return (d / n) ** (1 / p)

    def neighbors(self, data, rows=None):
        return sorted(rows or data.rows, key=lambda row: self.dist(row, data))
