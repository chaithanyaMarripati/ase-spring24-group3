import DATA
def eg_branch():
    d = DATA.new("../data/auto93.csv")

    result = branch(d)
    best, rest, evals = result.best, result.rest, result.evals

    print(l_o(best['mid'].cells), l_o(rest['mid'].cells))
    print(evals)