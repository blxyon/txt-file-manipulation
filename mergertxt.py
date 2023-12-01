import re
from datetime import datetime

def extract_datetime(line):
    # Extract the date and time information from the line using regular expression
    match = re.match(r"\[(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}:\d{2})\]", line)
    if match:
        date_str, time_str = match.groups()
        try:
            return datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M:%S")
        except ValueError as e:
            print(f"Error parsing datetime for line: {line.strip()}. Error: {e}")
    return None

def merge_and_sort(file1_path, file2_path, file3_path, output_path):
    # Read contents of all three files
    with open(file1_path, 'r', encoding='utf-8') as file1, \
         open(file2_path, 'r', encoding='utf-8') as file2, \
         open(file3_path, 'r', encoding='utf-8') as file3:
        lines = file1.readlines() + file2.readlines() + file3.readlines()

    # Extract and sort based on date and time
    sorted_lines = sorted(lines, key=lambda x: extract_datetime(x) or datetime.max)

    # Write sorted lines to the output file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(sorted_lines)

if __name__ == "__main__":
    file1_path = "file1.txt"  # Replace with the actual path of your first file
    file2_path = "file2.txt"  # Replace with the actual path of your second file
    file3_path = "file3.txt"  # Replace with the actual path of your third file
    output_path = "merged_output.txt"  # Replace with the desired output path

    merge_and_sort(file1_path, file2_path, file3_path, output_path)
    print("Merging and sorting completed.")