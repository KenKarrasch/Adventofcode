import re

f = open('24-13.txt').read().split('\n\n')

md = []
for i in f:
    numbers = re.findall(r'-?\d+', i)
    md.append(list(map(int, numbers)))
print(md)

def calculate_button_presses(Ax, Ay, Bx, By, X, Y):
    
    determinant = Ax * By - Ay * Bx
    
    if determinant == 0:
        return None  # No solution exists
    
    a = (X * By - Y * Bx) / determinant
    b = (Ax * Y - Ay * X) / determinant
    
    # Check if a and b are integers
    if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
        return int(a), int(b)
    else:
        return None  # No integer solution exists

tly = 0
for i in md:
    Ax, Ay, Bx, By, X, Y = i[0],i[1],i[2],i[3],10000000000000 + i[4],10000000000000 + i[5]
    print(Ax, Ay, Bx, By, X, Y)
    result = calculate_button_presses(Ax, Ay, Bx, By, X, Y)
    if result:
        presses_A, presses_B = result
        tly += presses_A * 3 + presses_B
        print(f"Press A {presses_A} times and B {presses_B} times")
    else:
        print("No solution exists")

print(tly)
