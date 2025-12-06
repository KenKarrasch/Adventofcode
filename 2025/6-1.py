f = open('25-6.txt').read().split('\n')
#  6     148    935  **

fs = []
op = []

for i in f[0:-1]:
    fs.append([int(x) for x in i.split()])

op = f[-1].split()

def add(cl):
    sm = 0
    for i in range(len(fs)):
        sm += fs[i][cl]
    return sm

def mult(cl):
    sm = 1
    for i in range(len(fs)):
        sm *= fs[i][cl]
    return sm

tly = 0
for i in range(len(op)):
    if op[i] == '+':
        tly += add(i)
    if op[i] == '*':
        tly += mult(i)
print(tly)
