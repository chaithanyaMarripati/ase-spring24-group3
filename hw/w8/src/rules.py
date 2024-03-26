from utils import powerset
from rule import Rule
from config import the

class Rules:
    def __init__(self, ranges, goal, rowss):
        self.sorted = []
        self.goal = goal
        self.rowss = rowss
        self.LIKE = 0
        self.HATE = 0
        self.likeHate()
        for range_ in ranges:
            range_.scored = self.score(range_.y)
        self.sorted = self.top(self.try_(self.top(ranges)))

    def likeHate(self):
        for y, rows in self.rowss.items():
            if y == self.goal:
                self.LIKE += len(rows)
            else:
                self.HATE += len(rows)

    def score(self, outcomes):
        like = sum(1 for outcome in outcomes if outcome == self.goal)
        hate = sum(1 for outcome in outcomes if outcome != self.goal)
        like /= (self.LIKE + the.tiny)
        hate /= (self.HATE + the.tiny)
        return 0 if hate > like else (like ** the.Support) / (like + hate)

    def try_(self, ranges):
        rule_set = []
        for subset in powerset(ranges):
            if subset:
                rule = Rule(subset)
                rule.scored = self.score(rule.selectss(self.rowss))
                if rule.scored > the.threshold:  
                    rule_set.append(rule)
        return rule_set

    def top(self, rule_set):
        rule_set.sort(key=lambda rule: rule.scored, reverse=True)
        return rule_set[:the.Beam]  