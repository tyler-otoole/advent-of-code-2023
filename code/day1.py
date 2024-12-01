def sum_first_last_digits(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            first_digit = None
            last_digit = None
            
            # Find the first digit in the line
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break
            
            # Find the last digit in the line
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break
            
            if first_digit is not None and last_digit is not None:
                combined_number = int(first_digit + last_digit)
                total_sum += combined_number
    
    return total_sum

# Example usage
file_path = 'data/input/day1.txt'  # Replace with your file path
result = sum_first_last_digits(file_path)
print(result)

