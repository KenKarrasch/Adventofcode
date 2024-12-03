
# Online Python - IDE, Editor, Compiler, Interpreter

f = open("24-3.txt").read()

import re

def calculate_mul_sum(text):
    pattern = r'(don\'t\(\)|do\(\)|mul\(\d+,\d+\))'
    matches = re.findall(pattern, text)
    
    total = 0
    ignore = False
    
    for match in matches:
        if match == "don't()":
            ignore = True
        elif match == "do()":
            ignore = False
        elif not ignore and match.startswith("mul"):
            x, y = map(int, re.findall(r'\d+', match))
            total += x * y
    
    return total

text = f
result = calculate_mul_sum(text)
print('part 2', result)  
