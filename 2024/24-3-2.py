
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
            if 1000 > int(match.split(',')[0].split('(')[1]) > -1:
                if 1000 > int(match.split(',')[1].split(')')[0]) > -1:
                    x, y = re.findall(r'\d+', match)            
                    total += int(x) * int(y)                
    return total

text = f
result = calculate_mul_sum(text)
print('part 2', result)  
