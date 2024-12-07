from itertools import product

f = open("24-7.txt").read().split('\n')

target = []
numbers = []

for i in f:
    target.append(int(i.split(':')[0]))
    numbers.append([int(n) for n in i.split(':')[1].split()])

#print(target)
#print(numbers)
   

def can_reach_target(numbers, target):
    # Generate all combinations of operations ('+', '*') for len(numbers) - 1 operations
    operations = list(product(['+', '*'], repeat=len(numbers) - 1))
    
    for ops in operations:
        # Start with the first number
        result = numbers[0]
        expression = str(numbers[0])
        
        # Apply the operations in order
        for i, op in enumerate(ops):
            if op == '+':
                result += numbers[i + 1]
                expression += f" + {numbers[i + 1]}"
            elif op == '*':
                #print(numbers[i + 1])
                result *= numbers[i + 1]
                expression += f" * {numbers[i + 1]}"
        
        # Check if the result matches the target
        if result == target:
            return True, expression
    
    # If no combination works
    return False, None

tly = 0

for i in range(len(f)):
    found, expression = can_reach_target(numbers[i], target[i])
    if found:
        print(f"Target {target} can be reached using: {expression}")
    else:
        print(f"Target {target} cannot be reached with the given numbers.")
    if(found)  : 
        tly += target[i]
    print(f"Can reach target: {expression}")

print(tly)

    
