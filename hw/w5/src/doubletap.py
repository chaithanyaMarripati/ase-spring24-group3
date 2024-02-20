import DATA
import branch

def doubletap():
    d = DATA.new("../data/auto93.csv")

    result1 = branch(d)
    best1, rest1, evals1 = result1.best, result1.rest, result1.evals

    result2 = branch(best1)
    best2, _, evals2 = result2.best, result2.rest, result2.evals

    print(l_o(best2['mid'].cells), l_o(rest1['mid'].cells))
    print(evals1 + evals2)