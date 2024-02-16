import os
from utils import read_csv_to_list
from DATA import DATA
def gate20():
    file_path = '../data/auto93.csv' 
    data_rows = read_csv_to_list(file_path)

    BUDGET0 = 4
    BUDGET = 16
    SOME = 0.5

    aggregated_outputs = {"print1": [], "print2": [], "print3": [], "print4": [], "print5": [], "print6": []}

    for _ in range(20):
        d = DATA(data_rows)
        gate_outputs = d.gate(BUDGET0, BUDGET, SOME)

        for key in aggregated_outputs:
            aggregated_outputs[key].extend(gate_outputs[key])

    output_file_path = os.path.join('..', 'w4_output.out')
    
    with open(output_file_path, 'w') as out_file:
        for key, values in aggregated_outputs.items():
            out_file.write(f"{key}:\n")
            for value in values:
                out_file.write(f'{value[0]},{value[1]},{value[2]}\n')
            out_file.write("======================\n")

if __name__ == "__main__":
    gate20()


