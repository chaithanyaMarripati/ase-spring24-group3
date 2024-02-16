import math
from COLS import COLS
from ROW import ROW
import random
class DATA:
    def __init__(self, rows):
        self.rows = [ROW(row) for row in rows]
        self.cols = {'x': [], 'y': []}  
        self.cols['x'] = [0, 1, 2]  
        self.cols['y'] = [3] 

    def add(self, row):
        if not self.cols:
            self.cols = COLS(row.cells)
        else:
            self.rows.append(row)

    def bestRest(self, rows, want):
        sorted_rows = sorted(rows, key=lambda row: row.d2h(self))
        return sorted_rows[:want], sorted_rows[want:]

    def gate(self, budget0, budget, some):        
        shuffled_rows = random.sample(self.rows, len(self.rows))
        results = {"print1": [], "print2": [], "print3": [], "print4": [], "print5": [], "print6": []}

        for row in shuffled_rows[:6]:
            results["print1"].append([row.values[5], row.values[6], row.values[7]])  # Assuming indices 4, 5, 6

        for row in shuffled_rows[:50]:
            results["print2"].append([row.values[5], row.values[6], row.values[7]])

        sorted_rows = sorted(self.rows, key=lambda row: row.d2h(self))
        results["print3"].append([sorted_rows[0].values[5], sorted_rows[0].values[6], sorted_rows[0].values[7]]) if sorted_rows else []

        lite = shuffled_rows[:budget0]
        dark = shuffled_rows[budget0:]

        for i in range(1, budget + 1):
            if dark:
                selected_row = random.choice(dark)
                lite.append(selected_row)
                dark.remove(selected_row)
                results["print4"].append([selected_row.values[5], selected_row.values[6], selected_row.values[7]])
                results["print5"].append([selected_row.values[5], selected_row.values[6], selected_row.values[7]])  # Example logic
                results["print6"].append([lite[0].values[5], lite[0].values[6], lite[0].values[7]])  # Example logic

        return results
    def split(self, best, rest, lite, dark):
        selected = []
        max_score, todo = -math.inf, None
        for i, row in enumerate(dark):
            b = row.like(best)
            r = row.like(rest)
            if b > r:
                selected.append(row)
            score = (b + r) / abs(b - r + 1E-30)
            if score > max_score:
                max_score, todo = score, i
        return todo, selected