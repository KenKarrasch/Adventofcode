from itertools import product

f = open("24-7.txt").read().split('\n')

target = []
numbers = []

for i in f:
    target.append(int(i.split(':')[0]))
    numbers.append([int(n) for n in i.split(':')[1].split()])

#print(target)
#print(numbers)
   
def can_reach_target_iterative(numbers, target):
    """
    Iterative solution where concatenation applies to the running tally.
    """
    stack = [(0, 0, "")]  # (current_index, current_value, expression)

    while stack:
        index, current_value, expression = stack.pop()

        # If we've used all numbers, check if the target is met
        if index == len(numbers):
            if current_value == target:
                return True, expression
            continue

        # Get the next number
        next_number = numbers[index]

        # Add the next number
        stack.append((index + 1, current_value + next_number, f"{expression} + {next_number}" if expression else str(next_number)))

        # Multiply the next number
        stack.append((index + 1, current_value * next_number if current_value != 0 else next_number, f"{expression} * {next_number}" if expression else str(next_number)))

        # Concatenate the next number with the current_value
        if expression:
            concatenated_value = int(str(current_value) + str(next_number))
            stack.append((index + 1, concatenated_value, f"({expression} || {next_number})"))

    return False, None

tly = 0
for i in range(len(f)):
    found, expression = can_reach_target_iterative(numbers[i], target[i])
    if found:
        print(f"Target {target[i]} can be reached using: {expression}")
    else:
        print(f"Target {target[i]} cannot be reached with the given numbers.")
    if(found):
        tly += target[i]

print('part 2 -',tly)
