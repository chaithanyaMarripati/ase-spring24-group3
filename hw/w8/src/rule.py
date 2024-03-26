from range import RANGE
from utils import show_less

class Rule:
    def __init__(self, ranges):
        self.parts = {}  
        self.scored = 0
        for range_ in ranges:
            if range_.txt not in self.parts:
                self.parts[range_.txt] = []
            self.parts[range_.txt].append(range_)

    def _or(self, ranges, row):
        x = row.cells[ranges[0].at]
        if x == "?":
            return True
        for range_ in ranges:
            lo, hi = range_.x.lo, range_.x.hi
            if lo == hi and lo == x or lo <= x < hi:
                return True
        return False

    def _and(self, row):
        for ranges in self.parts.values():
            if not self._or(ranges, row):
                return False
        return True

    def selects(self, rows):
        selected_rows = []
        for row in rows:
            if self._and(row):
                selected_rows.append(row)
        return selected_rows

    def selectss(self, rowss):
        selected = {}
        for y, rows in rowss.items():
            selected[y] = len(self.selects(rows))
        return selected

    def show(self):
        ands = []
        for ranges in self.parts.values():
            ors = show_less(ranges)
            ands.append(" or ".join(range_.show() for range_ in ors))
        return " and ".join(ands)
