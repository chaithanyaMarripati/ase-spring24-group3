class SYM:
    def __init__(self, s=None, n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + self.has.get(x, 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        # Assuming l.entropy is defined elsewhere
        return l.entropy(self.has)

    def small(self):
        return 0

    def norm(self, x):
        return x

    def dist(self, x, y):
        return 1 if x == "?" and y == "?" else 0 if x == y else 1

    def bin(self, x):
        return x