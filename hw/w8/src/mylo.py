from DATA import DATA
from utils import *
from config import *
from range import RANGE

def main():
    saved_options = {}

    for key, value in cli(settings(help)).items():
        the[key] = value
        saved_options[key] = value
    for key, value  in saved_options.items():
        the[key] = value
        global Seed
        Seed = the['seed']

class mylo: 
    def __init__(self):
        pass
    
    def rnd(self, n, ndecs=None):
        if not isinstance(n, (int, float)):
            return n
        if n.is_integer():
            return n
        mult = 10 ** (ndecs or 2)
        return round(n * mult) / mult

    def shuffle(self, t):
        u = t[:]
        random.shuffle(u)
        return u
    
    def _ranges(self, cols, rowss):
        t = []
        for col in cols:
            for range in self._ranges1(col, rowss):
                t.append(range)
        return t
    
    def _ranges1(self, col, rowss):
        out = {}
        nrows = 0
        for y, rows in rowss.items():
            nrows += len(rows)
            for row in rows:
                x = row.cells[col.at]
                if x != "?":
                    bin = col.bin(x)
                    if bin not in out:
                        out[bin] = RANGE(the, col.at, col.txt, x)
                    out[bin].add(x, y)
        out = list(out.values())
        out.sort(key=lambda a: a.x['lo'])
        return out if hasattr(col, 'has') else self._mergeds(out, nrows /the.get('bins',16))
    
    def _mergeds(self, ranges, tooFew):
        i, t = 0, []
        while i < len(ranges):
            a = ranges[i]
            if i < len(ranges) - 1:
                both = a.merged(ranges[i+1], tooFew)
                if both:
                    a = both
                    i += 1
            t.append(a)
            i += 1
        if len(t) < len(ranges):
            return self._mergeds(t, tooFew)
        for i in range(1, len(t)):
            t[i].x['lo'] = t[i-1].x['hi']
        t[0].x['lo'] = -math.inf
        t[-1].x['hi'] = math.inf
        return t
    
    def bins(self):
        data = DATA('../data/auto93.csv')
        best, rest, _ = data.branch()
        likeRows = best.rows
        hateRows = rest.rows[:3 * len(likeRows)]
        self.shuffle(hateRows)


        def score(range):
            return range.score("LIKE", len(likeRows), len(hateRows))

        t = []
        print("OUTPUT 1:")
        for col in data.cols.x:
            print("")
            for range in self._ranges1(data.cols.x[col], {"LIKE": likeRows, "HATE": hateRows}):
                print(str(range))
                t.append(range)
        
        t.sort(key=score, reverse=True)
        max_score = score(t[0])

        print("\nOUTPUT 2:")
        print("\n#scores:\n")
        for v in t[:the.get('Beam',1)]:
            if score(v) > max_score * .1:
                print(self.rnd(score(v)), v)

        print({"LIKE": len(likeRows), "HATE": len(hateRows)})


if __name__ == '__main__':
    main()
    mylo().bins()
