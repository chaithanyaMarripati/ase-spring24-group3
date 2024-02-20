import math

class ROW:
    def __init__(self, values):
        self.values = values

    def d2h(self, row):
        heaven_values = [data.cols.all[y].heaven for y in row.cols.y]
        if len(row.cols.y) == 0:
            return math.inf  # or handle this case based on your requirements
        norm = lambda c, x: (x - data.cols.all[c].lo) / (data.cols.all[c].hi - data.cols.all[c].lo + 1E-30)
        goals_distance = sum((heaven - norm(y, row.values[y]))**2 for heaven, y in zip(heaven_values, row.cols.y))
        
        return math.sqrt(goals_distance / len(row.cols.y))

    def likes(self, datas):
        n, n_hypotheses = 0, 0
        for data in datas:
            n += len(data.rows)
            n_hypotheses += 1
        most, out = None, None
        for k, data in enumerate(datas, start=1):
            tmp = self.like(data, n, n_hypotheses)
            if most is None or tmp > most:
                most, out = tmp, k
        return out, most

    # def like(self, data, n, n_hypotheses):
    #     prior = (len(data.rows) + 1) / (n + 1 * n_hypotheses)
    #     out = math.log(prior)
    #     for col in data.cols.x.values():
    #         v = self.values[col.at]
    #         if v != "?":
    #             inc = col.like(v, prior)
    #             out += math.log(inc)
    #     return math.exp(out)
    def like(self, data, n, nHypotheses):
        prior = (len(data.rows) + 1) / (n + 1 * nHypotheses)
        out = math.log(prior)
        for col in data.cols.x.values():
            v = self.values[col.at]
            if v != "?":
                inc = col.like(v, prior)
                try:
                    out += math.log(inc)
                except ValueError:
                    return 0.0
        return math.exp(1) ** out
