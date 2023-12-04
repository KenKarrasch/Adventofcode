# Chat GPT solution - part 1 only
#
# The query:
# "in python, if I have a file with a series of games per line, remove everything before ':', there 
# is a set of numbers on the left and a set of numbers on the right, separated by a '|',  in each 
# line work out how many common numbers there are between left and right.  Then with the count for 
# each line get pow(2,count), (if count is 0, use 0 instead), then add up the numbers, divide the end result by 2"
#
# 12 min to solve manually, 9 min to work out the query for ChatGPT, ChatGPT wins (against me) 
#

def process_file(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            # Extract everything after ':'
            line = line.split(':', 1)[-1].strip()

            # Split the line into left and right sides
            left, right = map(str.strip, line.split('|'))

            # Extract numbers from the left and right sides
            left_numbers = set(map(int, left.split()))
            right_numbers = set(map(int, right.split()))

            # Find common numbers
            common_numbers = left_numbers.intersection(right_numbers)

            # Calculate the count of common numbers
            count = len(common_numbers)

            # Calculate pow(2, count) and add it to the total sum (use 0 if count is 0)
            total_sum += pow(2, count) if count > 0 else 0

    # Divide the final result by 2
    final_result = total_sum / 2

    return final_result

file_path = '23-4.txt'  # Replace with the path to your file
result = process_file(file_path)
print(f'Final result (sum of pow(2, count) divided by 2): {result}')
