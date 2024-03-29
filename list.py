def process_lines(file_path):
    processed_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) < 3 or '?' in line or '--' in line:
                continue  # Skip lines based on the specified conditions
            
            # Check if XP (the third element from the end) is '0' after removing commas
            xp_value = parts[-3].replace(',', '')
            if xp_value.isdigit() and int(xp_value) == 0:
                continue  # Skip lines with 0 XP

            # Remove first instance of duplicate name
            name = parts[0]
            rest_of_line = '\t'.join(parts[1:])
            if rest_of_line.startswith(name + '\t'):
                processed_line = rest_of_line[len(name) + 1:]  # +1 for the tab character
            else:
                processed_line = rest_of_line
            
            processed_lines.append(name + '\t' + processed_line)
    
    return processed_lines

def write_processed_lines(output_file_path, processed_lines):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for line in processed_lines:
            file.write(line + '\n')

if __name__ == "__main__":
    input_file_path = 'list.txt'
    output_file_path = 'list2.txt'
    processed_lines = process_lines(input_file_path)
    write_processed_lines(output_file_path, processed_lines)
    print("Processing completed.")
