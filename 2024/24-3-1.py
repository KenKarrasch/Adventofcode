
# Online Python - IDE, Editor, Compiler, Interpreter

# another 5 min solve, I'm sure the harder ones are coming.

f = open("24-3.txt").read()

import re

def calculate_mul_sum(text):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, text)
    total = sum(int(x) * int(y) for x, y in matches)
    return total
text = f
result = calculate_mul_sum(text)
print('part 1 -', result)  
