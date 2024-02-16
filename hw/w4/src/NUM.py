import math

class NUM:
    def __init__(self, s, n=0):
        self.txt = s or " "
        self.at = n
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -math.inf
        self.lo = math.inf
        self.heaven = 0 if (s or "").endswith("-") else 1

    def add(self, x):
        if x != "?":
            x = float(x)
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return math.sqrt(self.m2 / (self.n - 1)) if self.n >= 2 else 0

    def norm(self, x):
        return (x - self.lo) / (self.hi - self.lo + 1E-30) if x != "?" else x

    def like(self, x, _=None):
        mu, sd = self.mid(), self.div() + 1E-30
        nom = math.exp(-0.5 * ((x - mu) ** 2) / (sd ** 2))
        denom = sd * 2.71828 + 1E-30
        return nom / denom
