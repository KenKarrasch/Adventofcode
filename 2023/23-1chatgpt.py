#ChatGPT input
# in python read in a file that has lines with letters and numbers, extract the first and last digit in each string to form a two digit number, (if there is only one digit, use digit as the first and last), then add the numbers

# 5 min solve with Chat GPT, This solution was done after I completed my own solution

def process_file(file_path):
    total_sum = 0

    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Extract digits from the line
            digits = [char for char in line if char.isdigit()]

            # If there are no digits in the line, skip to the next line
            if not digits:
                continue

            # Extract the first and last digits
            first_digit = int(digits[0])
            last_digit = int(digits[-1])

            # Form a two-digit number by concatenating the first and last digits
            two_digit_number = int(str(first_digit) + str(last_digit))

            # Add the two-digit number to the total sum
            total_sum += two_digit_number

    return total_sum

# Example usage
file_path = '23-1.txt'  # Replace 'your_file.txt' with the actual file path
result = process_file(file_path)
print(f'Total sum of two-digit numbers: {result}')
