import math
class ROW:
    k = 1 
    def __init__(self, t):
        self.cells = t

    def d2h(self, data):
        d, n = 0, 0
        for col in data.cols.y.values():
            n += 1
            d += (col.heaven - col.norm(self.cells[col.at]))**2
        return math.sqrt(d) / math.sqrt(n)

    def likes(self, datas):
        n, nHypotheses = 0, 0
        for k, data in datas.items():
            n += len(data.get("rows", []))
            nHypotheses += 1
        most, out = None, None
        for k, data in datas.items():
            tmp = self.like(data, n, nHypotheses)
            if most is None or tmp > most:
                most, out = tmp, k
        return out, most

    def like(self, data, n, nHypotheses):
        prior = (len(data.get("rows", [])) + self.k) / (n + self.k * nHypotheses)
        out = math.log(prior)
        for _, col in data["cols"]["x"].items():
            v = self.cells.get(col.at, "?")  # Use get method to handle missing keys
            if v != "?":
                inc = col.like(v, prior)
                out += math.log(inc)
        return math.exp(1)**out 

