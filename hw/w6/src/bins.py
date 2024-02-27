from utils import *

def eg_bins(the_Beam):
    data = read_csv("../data/auto93.csv")

    best, rest = data.iloc[:len(data)//2], data.iloc[len(data)//2:]

    LIKE = best.copy()
    HATE = rest.sample(n=3 * len(LIKE))

    def score(range):
        return range.score("LIKE", len(LIKE), len(HATE))

    t = []
    for col in data.columns[:-1]:  
        print("")
        for range in _ranges1(col, {"LIKE": LIKE, "HATE": HATE}):
            print(range)
            t.append(range)

    t.sort(key=score, reverse=True)

    max_score = score(t[0])

    print("\n#scores:\n")
    for v in t[:the_Beam]:
        if score(v) > max_score * 0.1:
            print(np.random.choice(score(v)), v)

    print({"LIKE": len(LIKE), "HATE": len(HATE)})

