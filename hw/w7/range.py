import math

class RANGE:
    def __init__(self, at, txt, lo, hi=None):
        self.at = at
        self.txt = txt
        self.scored = 0
        self.x = {'lo': lo, 'hi': hi or lo}
        self.y = {}

    def add(self, x, y):
        self.x['lo'] = min(self.x['lo'], x)
        self.x['hi'] = max(self.x['hi'], x)
        self.y[y] = self.y.get(y, 0) + 1

    def show(self):
        lo, hi, s = self.x['lo'], self.x['hi'], self.txt
        if lo == -math.inf:
            return f"{s} < {hi}"
        if hi == math.inf:
            return f"{s} >= {lo}"
        if lo == hi:
            return f"{s} == {lo}"
        return f"{lo} <= {s} < {hi}"

    def score(self, goal, LIKE, HATE):
        return l.score(self.y, goal, LIKE, HATE)

    def merge(self, other):
        both = RANGE(self.at, self.txt, self.x['lo'])
        both.x['lo'] = min(self.x['lo'], other.x['lo'])
        both.x['hi'] = max(self.x['hi'], other.x['hi'])
        for t in [self.y, other.y]:
            for k, v in t.items():
                both.y[k] = both.y.get(k, 0) + v
        return both

    def merged(self, other, tooFew):
        both = self.merge(other)
        e1, n1 = l.entropy(self.y)
        e2, n2 = l.entropy(other.y)
        if n1 <= tooFew or n2 <= tooFew:
            return both
        if l.entropy(both.y) <= (n1 * e1 + n2 * e2) / (n1 + n2):
            return both


def _ranges(cols, rowss):
    t = []
    for col in cols:
        for range_ in _ranges1(col, rowss):
            t.append(range_)
    return t


def _ranges1(col, rowss):
    out, nrows = [], 0
    for y, rows in rowss.items():
        nrows += len(rows)
        for row in rows:
            x = row['cells'][col.at]
            if x != "?":
                bin_ = col.bin(x)
                out.append(RANGE(col.at, col.txt, x))
                out[bin_ - 1].add(x, y)
    out.sort(key=lambda a: a.x['lo'])
    return out if col.has else _mergeds(out, nrows / the.bins)


def _mergeds(ranges, tooFew):
    i, t = 1, []
    while i <= len(ranges):
        a = ranges[i - 1]
        if i < len(ranges):
            both = a.merged(ranges[i], tooFew)
            if both:
                a = both
                i += 1
        t.append(a)
        i += 1
    if len(t) < len(ranges):
        return _mergeds(t, tooFew)
    for i in range(1, len(t)):
        t[i].x['lo'] = t[i - 1].x['hi']
    t[0].x['lo'] = -math.inf
    t[-1].x['hi'] = math.inf
    return t
