
# Online Python - IDE, Editor, Compiler, Interpreter

# another 5 min solve, I'm sure the harder ones are coming. Started late due to meetings

# ----> Edit: Amended to exclude edge cases where there a numbers larger than 3 digits, or zero length. Part 2 amended also.

#  Dawned on me on the way home on the train. Also spotted by peer puzzle solver.

f = open("24-3.txt").read()

import re

def calculate_mul_sum(text):
    pattern = r'mul\(\d+,\d+\)'  #r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, text)
    total = 0
    ignore = False    
    for match in matches: 
        if match.startswith("mul"):                 
            if 1000 > int(match.split(',')[0].split('(')[1]) > -1:
                if 1000 > int(match.split(',')[1].split(')')[0]) > -1:
                    x, y = re.findall(r'\d+', match)            
                    total += int(x) * int(y)  
    
    return total
text = f
result = calculate_mul_sum(text)
print('part 1 -', result)   
