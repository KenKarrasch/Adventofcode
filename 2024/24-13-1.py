import re

f = open('24-13.txt').read().split('\n\n')

md = []
for i in f:
    numbers = re.findall(r'-?\d+', i)
    md.append(list(map(int, numbers)))
print(md)

def calculate_button_presses(Ax, Ay, Bx, By, X, Y):
    # Calculate the difference between target and initial position
    dx = X - 0  # Assuming we start at (0,0)
    dy = Y - 0

    # Solve the system of linear equations
    # a * Ax + b * Bx = dx
    # a * Ay + b * By = dy
    
    determinant = Ax * By - Ay * Bx
    
    if determinant == 0:
        return None  # No solution exists
    
    a = (dx * By - dy * Bx) / determinant
    b = (Ax * dy - Ay * dx) / determinant
    
    # Check if a and b are integers
    if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
        return int(a), int(b)
    else:
        return None  # No integer solution exists

# Example usage
Ax, Ay = 0, 0  # Initial position
Bx, By = 2, 3  # Movement when pressing B
X, Y = 10, 15  # Target position

tly = 0
for i in md:
    Ax, Ay, Bx, By, X, Y = i[0],i[1],i[2],i[3],i[4],i[5]
    print(Ax, Ay, Bx, By, X, Y)
    result = calculate_button_presses(Ax, Ay, Bx, By, X, Y)
    if result:
        presses_A, presses_B = result
        tly += presses_A * 3 + presses_B
        print(f"Press A {presses_A} times and B {presses_B} times")
    else:
        print("No solution exists")

print(tly)
