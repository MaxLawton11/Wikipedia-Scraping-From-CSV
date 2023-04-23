import os

MAX_LINES_PER_FILE = 5000
input_filename = "DataSet.text"

input_file = open(input_filename, "r")
output_file = None

line_count = 0
output_file_count = 0

for line in input_file:
    if line.startswith('"""'):
        if output_file is not None and line_count >= MAX_LINES_PER_FILE:
            output_file.close()
            output_file_count += 1
            output_file_name = f"DataSet/data_{output_file_count}.txt"
            output_file = open(output_file_name, "w")
            line_count = 0
        elif output_file is None:
            output_file_count += 1
            output_file_name = f"DataSet/data_{output_file_count}.txt"
            output_file = open(output_file_name, "w")
        output_file.write(line)
    elif output_file is not None:
        output_file.write(line)
        line_count += 1
    
if output_file is not None:
    output_file.close()

input_file.close()
