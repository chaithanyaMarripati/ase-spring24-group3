import random

class DATA:
    def gate(self, budget0, budget, some):
        rows = random.sample(self.rows, len(self.rows))
        lite = rows[:budget0]
        dark = rows[budget0:]

        stats, bests = [], []

        for i in range(1, budget + 1):
            best, rest = self.bestRest(lite, len(lite) ** some)
            todo, selected = self.split(best, rest, lite, dark)
            stats.append(selected.mid())
            bests.append(best.rows[0])
            lite.append(dark.pop(todo))

        return stats, bests