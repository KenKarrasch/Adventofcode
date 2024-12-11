f = open('25-11.txt').read()
#5 89749 6061 43 867 1965860 0 206250'

numbers = f.split()

def transform_numbers(numbers):
    result = []
    for num_str in numbers:
        # Rule 1: If the number is 0, convert to 1
        if num_str == '0':
            result.append('1')
        # Rule 2: If the number has an even number of digits, split in half
        elif len(num_str) % 2 == 0:
            mid = len(num_str) // 2
            result.extend([str(int(num_str[:mid])), str(int(num_str[mid:]))])
        # If neither rule 1 nor rule 2 applies, multiply by 2024
        else:
            result.append(str(int(num_str) * 2024))
    return result

# Example usage:
nmbers = ['0', '12', '345', '6789', '10']
for i in range(25):
    print(i)
    transformed = transform_numbers(numbers)
    #print(transformed)
    numbers = transformed[:]
print(len(transformed))
