import random
from COLS import COLS
from ROW import ROW

class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = None

    def add(self, row):
        if not self.cols:
            self.cols = COLS(row.values)
        else:
            self.rows.append(row)

    def mid(self, cols=None):
        u = [col.mid() for col in cols or self.values()]
        return ROW(u)

    def div(self, cols=None):
        u = [col.div() for col in cols or self.cols.all.values()]
        return ROW(u)

    def small(self):
        u = [col.small() for col in self.cols.all.values()]
        return ROW(u)

    def stats(self, cols=None, fun=None, ndivs=None):
        u = {".N": len(self.rows)}
        for col in self.cols.y.values():
            u[col.txt] = round(getattr(col, fun or "mid")(), ndivs)
        return u
    
    def centroid(lst):
        sorted_lst = sorted(lst)
        n = len(sorted_lst)
        if n % 2 == 1:
            return sorted_lst[n // 2]
        else:
            mid1 = sorted_lst[n // 2 - 1]
            mid2 = sorted_lst[n // 2]
            return (mid1 + mid2) / 2
    
    def gate(self, budget0, budget, some):
        results = {"print1 (Top 6)": [], "print2 (Top 50)": [], "print3 (Most)": [], "print4 (Rand)": [], "print5 (Mid)": [], "print6 (Top)": []}
        rows = random.sample(self.rows, len(self.rows))
        #top 6
        for row in rows[:6]:
            results["print1 (Top 6)"].append([row.values[5], row.values[6], row.values[7]])
        #top 50
        for row in rows[:50]:
            results["print2 (Top 50)"].append([row.values[5], row.values[6], row.values[7]])
        sorted_rows = sorted(self.rows, key=lambda row: row.d2h(self))

        results["print3 (Most)"].append([sorted_rows[0].values[5], sorted_rows[0].values[6], sorted_rows[0].values[7]]) if sorted_rows else []

        lite = rows[:budget0]
        dark = rows[budget0:]
        stats, bests = [], []
        for i in range(budget):
            best, rest = self.bestRest(lite, len(lite)**some)
            todo, selected = self.split(best, rest, lite, dark)
            selected_dark_rows = random.sample(dark, budget0 + i)
            centroid_dark_y_values = [row.values[5:8] for row in selected_dark_rows]
            centroid_dark = [round(sum(float(val) for val in col) / len(col), 2) for col in zip(*centroid_dark_y_values)]
            results["print4 (Rand)"].append(centroid_dark)
            centroid_selected_y_values = [list(map(float, row.values[5:8])) for row in selected]
            centroid_selected = [round(sum(col) / len(col), 2) for col in zip(*centroid_selected_y_values)]
            results["print5 (Mid)"].append(centroid_selected)
            results["print6 (Top)"].append(best.rows[0].values[5:8])
            print(results["print6 (Top)"])
            bests.append(best.rows[0])
            lite.append(dark.pop(todo))
        return results
    
    
    def split(self, best, rest, lite, dark):
        selected = []
        max_score, todo = float('-inf'), None
        for i, row in enumerate(dark):
            r = row.like(best, len(lite), 2)
            b = row.like(rest, len(lite), 2)
            if b >= r:
                selected.append(row)
            score = abs(b + r) / abs(b - r + 1E-300)
            if score > max_score:
                max_score, todo = score, i
        return todo, selected

    def bestRest(self, rows, want):
        rows.sort(key=lambda row: row.d2h(self))
        # best = rows[:int(want)+1]
        # rest = rows[int(want)+1:]
        # d1 = DATA(best)
        # d2 = DATA(rest)
        # for r in rest:
        #     d2.add(r)
        # for b in best:
        #     d1.add(b)
        best = []
        rest = []
        for i, row in enumerate(rows):
            if i <= want:
                best.append(row)
            else:
                rest.append(row)
        d1 = DATA(best)
        d2 = DATA(rest)
        for b in best:
            d1.add(b)
        for r in rest:
            d2.add(r)
        return d1,d2

    # def gate(self, budget0, budget, some):        
    #     shuffled_rows = random.sample(self.rows, len(self.rows))
    #     results = {"print1": [], "print2": [], "print3": [], "print4": [], "print5": [], "print6": []}
    #     #Top 6
    #     for row in shuffled_rows[:6]:
    #         results["print1"].append([row.values[5], row.values[6], row.values[7]])

    #     #Top 50
    #     for row in shuffled_rows[:50]:
    #         results["print2"].append([row.values[5], row.values[6], row.values[7]])

    #     sorted_rows = sorted(self.rows, key=lambda row: row.d2h(self))
    #     results["print3"].append([sorted_rows[0].values[5], sorted_rows[0].values[6], sorted_rows[0].values[7]]) if sorted_rows else []

    #     lite = shuffled_rows[:budget0]
    #     dark = shuffled_rows[budget0:]
    #     stats = []
    #     bests = []
    #     for i in range(1, 1+budget):
    #         best, rest = self.bestRest(lite, len(lite)**some)
    #         todo, selected = self.split(best, rest, lite, dark)
    #         selected_dark_rows = random.sample(dark, budget0 + i)
    #         centroid_dark_y_values = [row.values[5:8] for row in selected_dark_rows]
    #         centroid_dark = [round(sum(float(val) for val in col) / len(col), 2) for col in zip(*centroid_dark_y_values)]
    #         results["print4"].append(centroid_dark)
    #         centroid_selected_y_values = [row.values[5:8] for row in selected.rows]
    #         centroid_selected = [round(sum(col) / len(col), 2) for col in zip(*centroid_selected_y_values)]
    #         results["print5"].append(centroid_selected)
    #         results["print6"].append(best.rows[0].values[5:8])
    #         print(results["print5"])
    #         stats.append(selected.rows.values.mid())
    #         bests.append(best.rows[0])
    #         lite.append(dark.pop(todo))
    #     print("stats: ", stats)
    #     print("bests: ", bests)
    #     return results
    #     #     if dark:
    #     #         selected_row = random.choice(dark)
    #     #         lite.append(selected_row)
    #     #         dark.remove(selected_row)
    #     #         results["print4"].append([selected_row.values[5], selected_row.values[6], selected_row.values[7]])
    #     #         results["print5"].append([selected_row.values[5], selected_row.values[6], selected_row.values[7]])  # Example logic
    #     #         results["print6"].append([lite[0].values[5], lite[0].values[6], lite[0].values[7]])  # Example logic

    #     # return results

    # # def split(self, best, rest, lite, dark):
    # #     selected = []
    # #     max_score, todo = -math.inf, None
    # #     for i, row in enumerate(dark):
    # #         b = row.like(best, len(lite))
    # #         r = row.like(rest, len(lite))
    # #         if b > r:
    # #             selected.append(row)
    # #         score = (b + r) / abs(b - r + 1E-30)
    # #         if score > max_score:
    # #             max_score, todo = score, i
    # #     return todo, selected
    # def split(self, best, rest, lite, dark):
    #     selected = DATA(self.cols.names)
    #     max_score, todo = -math.inf, None
    #     for i, row in enumerate(dark):
    #         b = row.like(best, len(lite))
    #         r = row.like(rest, len(lite))
    #         print(f"Row {i + 1}: b = {b}, r = {r}")
    #         if b > r:
    #             selected.add(row)
    #         score = (b + r) / abs(b - r + 1E-30)
    #         print(f"Score: {score}")
    #         if score > max_score:
    #             max_score, todo = score, i

    #     print(f"Selected: {selected.rows}")
    #     print(f"Todo: {todo}")

    #     return todo, selected