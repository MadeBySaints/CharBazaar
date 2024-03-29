# Define the path to the input file and the output file
input_file_path = 'kills.txt'  # Change this to the path of your input file
output_file_path = 'kills2.txt'  # The processed output will be saved here

# Function to process each line of the input file
def process_line(line):
    parts = line.split('\t')  # Assuming the file is tab-separated
    if len(parts) >= 3:
        # Extract the Kills and Name, removing the " x" from the Kills
        kills = parts[1].strip().replace(' x', '')
        name = parts[2].strip()
        return f"{name} - {kills}"
    return None

# Read the input file, process each line, and write the output to the new file
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    next(input_file)  # Skip the header line
    for line in input_file:
        processed_line = process_line(line)
        if processed_line:
            output_file.write(processed_line + '\n')

print(f"Processed data written to {output_file_path}")
