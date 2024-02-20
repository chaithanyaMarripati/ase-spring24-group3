from pathlib import Path
def parse_line(line, delimiter=','):
    return [x.strip() for x in line.split(delimiter)]

def read_csv_to_list(file_path, delimiter=','):
    data_rows = []
    file_path = Path(file_path)
    
    with file_path.open('r') as file:
        # Skip the header line if your CSV has headers
        next(file)
        for line in file:
            values = parse_line(line, delimiter)
            if values:  # Ensure the line is not empty
                data_rows.append(values)
    
    return data_rows