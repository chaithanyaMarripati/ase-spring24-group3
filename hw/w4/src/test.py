import os
from utils import read_csv_to_list
from DATA import DATA
from ROW import ROW

# Perform 20 runs of the gate method
file_path = '../data/auto93.csv' 
data_rows = read_csv_to_list(file_path)
print(data_rows)
BUDGET0 = 4
BUDGET = 16
SOME = 0.5
d = DATA(data_rows)

for row_data in data_rows:
    row = ROW(row_data)
    d.add(row)

num_runs = 20
results_gate = {"print1": [], "print2": [], "print4": [], "print5": [], "print6": []}
for _ in range(num_runs):
    results = d.gate(BUDGET0, BUDGET, SOME)
    results_gate["print1"].extend(results["print1 (Top 6)"])
    results_gate["print2"].extend(results["print2 (Top 50)"])
    results_gate["print4"].extend(results["print4 (Rand)"])
    results_gate["print5"].extend(results["print5 (Mid)"])
    results_gate["print6"].extend(results["print6 (Top)"])

average_print1 = sum([sum(map(float, row)) for row in results_gate["print1"]]) / len(results_gate["print1"])
    
average_print2 = sum([sum(map(float, row)) for row in results_gate["print2"]]) / len(results_gate["print2"])

average_print4 = sum([sum(map(float, row)) for row in results_gate["print4"]]) / len(results_gate["print4"])

average_print5 = sum([sum(map(float, row)) for row in results_gate["print5"]]) / len(results_gate["print5"])

average_print6 = sum([sum(map(float, row)) for row in results_gate["print6"]]) / len(results_gate["print6"])

# Print or compare the results
print("Average Print1 (Gate):", average_print1)
print("Average Print2 (Gate):", average_print2)
print("Average Print4 (Gate):", average_print4)
print("Average Print5 (Gate):", average_print5)
print("Average Print6 (Gate):", average_print6)