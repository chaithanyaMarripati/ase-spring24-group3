import os
from utils import read_csv_to_list
from DATA import DATA
from ROW import ROW

def gate20():
    file_path = '../data/auto93.csv' 
    data_rows = read_csv_to_list(file_path)
    print(data_rows)
    BUDGET0 = 4
    BUDGET = 16
    SOME = 0.5

    aggregated_outputs = {"print1 (Top 6)": [], "print2 (Top 50)": [], "print3 (Most)": [], "print4 (Rand)": [], "print5 (Mid)": [], "print6 (Top)": []}

    for _ in range(20):
        d = DATA(data_rows)
        # Assuming you want to add all rows to the DATA instance
        for row_data in data_rows:
            row = ROW(row_data)
            print(row)
            d.add(row)
        gate_outputs = d.gate(BUDGET0, BUDGET, SOME)
        for key in aggregated_outputs:
            aggregated_outputs[key].extend(gate_outputs[key])

    output_file_path = os.path.join('..', 'w4_output.out')
    
    with open(output_file_path, 'w') as out_file:
        for key, values in aggregated_outputs.items():
            out_file.write(f"{key}:\n")
            for value in values:
                if len(value) >= 3:
                    out_file.write(f'{value[0]},{value[1]},{value[2]}\n')
                else:
                    print("Not enough elements in 'value' list.")
            out_file.write("====================================================\n")

if __name__ == "__main__":
    gate20()


