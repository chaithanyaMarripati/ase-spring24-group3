import math
from NUM import NUM
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


# Example usage:
the_data = {"1": 10, "2": 15, "3": "?"}  # Example data for ROW instance
the = ROW(the_data)
datas = {
    "data1": {
        "cols": {"x": {1: NUM(), 2: NUM()}, "y": {3: NUM()}},
        "rows": [
            {"1": 10, "2": 15, "3": "?"}, 
            {"1": 12, "2": 18, "3": "?"}
        ]
    }
}

result = the.likes(datas)
print("Best data:", result[0])
print("Likelihood:", result[1])

