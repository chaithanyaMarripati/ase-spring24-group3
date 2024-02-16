import math
class SYM:
    def __init__(self, s, n=0, m=1):
        self.txt = s or " "
        self.at = n
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0
        self.m = m 

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = self.has.get(x, 0) + 1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        e = 0
        for v in self.has.values():
            p = v / self.n
            e -= p * math.log(p, 2)
        return e

    def like(self, x, prior):
        return (self.has.get(x, 0) + self.m * prior) / (self.n + self.m)