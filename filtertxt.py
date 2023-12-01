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

def filter_and_remove(file_path, output_path, filter_text):
    # Read contents of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Filter and remove lines containing the specified text
    filtered_lines = [line for line in lines if filter_text not in line]

    # Write filtered lines to the output file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(filtered_lines)

if __name__ == "__main__":
    input_path = "input_file.txt"  # Replace with the actual path of your input file
    output_path = "filtered_output.txt"  # Replace with the desired output path
    filter_text = "certain_string"  # Replace with the text you want to filter

    filter_and_remove(input_path, output_path, filter_text)
    print(f"Filtering and removing lines containing '{filter_text}' completed.")
