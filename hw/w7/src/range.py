import math
from config import *

class RANGE:
  def __init__(self, the, at, txt, lo, hi=None):
    self.at = at
    self.txt = txt
    self.scored = 0.0
    self.the = the
    self.x = {'hi': hi or lo, 'lo': lo}
    self.y = {}
    pass
  
  def entropy(self, t):
        n = sum(t.values())
        e = sum([-v/n * math.log(v/n, 2) for v in t.values()])
        return e, n
  
  def add(self, x, y):
    self.x['lo'] = min(self.x['lo'], x)
    self.x['hi'] = max(self.x['hi'], x)
    self.y[y] = self.y.get(y, 0) + 1
  
  def scores(self, t, goal, LIKE, HATE):
        like, hate, tiny = 0, 0, 1E-30
        for klass, n in t.items():
            if klass == goal:
                like += n
            else:
                hate += n
        like, hate = like / (LIKE + tiny), hate / (HATE + tiny)
        if hate > like:
            return 0
        else:
            return like ** the.get('Support',2) / (like + hate)
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
    return self.scores(self.y, goal, LIKE, HATE)
  
  def merge(self, other):
    both = RANGE(self.the, self.at, self.txt, self.x['lo'])
    both.x['lo'] = min(self.x['lo'], other.x['lo'])
    both.x['hi'] = max(self.x['hi'], other.x['hi'])
    for t in [self.y, other.y]:
        for k, v in t.items():
            both.y[k] = both.y.get(k, 0) + v
    return both
   
  def merged(self, other, tooFew):
    both = self.merge(other)
    e1, n1 = self.entropy(self.y)
    e2, n2 = self.entropy(other.y)
    if n1 <= tooFew or n2 <= tooFew:
        return both
    e, n = self.entropy(both.y)
    if e <= (n1 * e1 + n2 * e2) / (n1 + n2):
        return both
      
  def __str__(self):
        return "{ at: " + str(self.at) + ", scored: " + str(self.scored) +  ", txt: " + self.txt + ", x: " + str(self.x) + ", y: " + str(self.y) + " }"

