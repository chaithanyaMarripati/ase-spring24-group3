'''Task-1: Count up how many classes are in each file, and the number of rows for each class.
Express that as a percetange of number of rows in those files.'''
import os
def analyze_csv(file_path):
    try:
        # Read the CSV file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Extracting headers and rows
        headers = lines[0].strip().split(',')
        rows = [line.strip().split(',') for line in lines[1:]]

        # Identifying the index of 'class!' column
        class_index = headers.index('class!')

        # Counting the occurrences of each class
        class_counts = {}
        for row in rows:
            class_ = row[class_index]
            class_counts[class_] = class_counts.get(class_, 0) + 1

        # Total number of rows
        total_rows = len(rows)

        # Calculate the percentage of rows for each class and prepare for the table
        table_data = []
        for class_, count in class_counts.items():
            percentage = (count / total_rows) * 100
            table_data.append([class_, count, f"{percentage:.2f}%", total_rows])

        # Add total classes row
        table_data.append(["Total Classes", len(class_counts), "100.00%", total_rows])

        # Determine the max width for each column
        col_widths = [max(len(str(row[i])) for row in table_data) + 7 for i in range(4)]

        # Create a horizontal line
        horizontal_line = "+" + "+".join("-" * col_width for col_width in col_widths) + "+"

        # Generate ASCII table with borders
        table = horizontal_line + "\n"
        header_row = ["Class", "Count", "Percentage", "Total Rows"]
        table += "|" + "|".join(header.ljust(col_width) for header, col_width in zip(header_row, col_widths)) + "|\n"
        table += horizontal_line + "\n"
        for row in table_data[:-1]:  # Exclude the last row (Total Classes) for now
            table += "|" + "|".join(str(item).ljust(col_widths[i]) for i, item in enumerate(row)) + "|\n"
        table += horizontal_line + "\n"
        # Now add the Total Classes row
        table += "|" + "|".join(str(item).ljust(col_widths[i]) for i, item in enumerate(table_data[-1])) + "|\n"
        table += horizontal_line

        return table

    except Exception as e:
        return f"An error occurred: {e}"

output_file_path = os.path.join('..', 'Task1_output.out')  # Go up one directory to w3

# Open the output file in write mode
with open(output_file_path, 'w') as out_file:
    for file_name in ['diabetes.csv', 'soybean.csv']:
        file_path = os.path.join('..', 'data', file_name)  # Adjust the path to the csv files
        analysis_result = analyze_csv(file_path)
        
        # Write the analysis result to the output file
        out_file.write(f'Analysing: {file_name}\n')
        out_file.write(analysis_result + '\n\n')
        
        # Also print the result to the console
        print(f'Analysing: {file_name}')
        print(analysis_result, '\n')
