# from utils import *
# from config import *
# from DATA import DATA
# from rules import *
# import range

# def rules():
#     for _ in range(1):
#         d = DATA(the["file"])
        
#         best0, rest, evals1 = d.branch(the["d"])
#         best, _, evals2 = best0.branch(the["D"])
#         print(evals1 + evals2 + the["D"] - 1)
#         LIKE = best.rows
#         HATE = shuffle(rest.rows)[1:3 * len(LIKE)]
#         rowss = {"LIKE": LIKE, "HATE": HATE}
    
#         for _, rule in enumerate(RULES(range.ranges(d.cols.x, rowss), "LIKE", rowss).sorted):
#             result = d.clone(rule.selects(rest.rows))
#             if len(result.rows) > 0:
#                 result.rows.sort(key=lambda a: a.d2h(d))
#                 print(rnd(rule.scored), rnd(result.mid().d2h(d)), rnd(result.rows[0].d2h(d)),
#                       o(result.mid().cells), "\t", rule.show())
from utils import *
from config import *
from DATA import DATA
from rules import *
import ranges
import sys

# Save the standard output stream to a variable
stdout_original = sys.stdout

# Define the file path
file_path = "../out/hw08.out"
def rules():
    # Open the file for writing
    with open(file_path, "w") as f:
        # Redirect standard output to the file
        sys.stdout = f
        print("score                mid selected                                            rule")
        print("------               -------------                                           ------")
        for k in range(1):
            d = DATA(the["file"])
            
            best0, rest, evals1 = d.branch(the["d"])
            best, _, evals2 = best0.branch(the["D"])
            # print(evals1 + evals2 + the["D"] - 1)
            LIKE = best.rows
            HATE = shuffle(rest.rows)[1:3 * len(LIKE)]
            # rest.shuffle(rest.rows)
            # HATE = rest.rows[1:3 * len(LIKE)]  # Use shuffled list
            rowss = {"LIKE": LIKE, "HATE": HATE}  
            for _, rule in enumerate(RULES(ranges.ranges(d.cols.x, rowss), "LIKE", rowss).sorted):
                result = d.clone(rule.selects(rest.rows))
                if len(result.rows) > 0:
                    result.rows.sort(key=lambda a: a.d2h(d))
                    mid_values = [rnd(val, 2) for val in result.mid().cells]
                    print(rnd(rule.scored), rnd(result.mid().d2h(d)), rnd(result.rows[0].d2h(d)), "\t" ,
                        o(mid_values), "\t\t\t", rule.show())
    # Restore the standard output
    sys.stdout = stdout_original
    print(f"Output saved to {file_path}")
                    