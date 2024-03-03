from DATA import DATA
from utils import *
from config import *

data = DATA('./data/auto93.csv')
print("--------TREE--------")
node, evals = data.tree(True)
node.show()
print("evals: ", evals)
    
    
print("\n\n\n--------BRANCH--------")
best, rest, evals = data.branch()
print("centroid of output cluster:\n", o(best.mid().cells))
print("evals: ",evals)
    
    
print("\n\n\n--------DOUBLE TAP--------")
best1, rest, evals1 = data.branch(32)
best2, _, evals2 = best1.branch(4)
print("centroid of best of 4 cluster:\n", o(best2.mid().cells))
print("evals: ", evals1 + evals2)


