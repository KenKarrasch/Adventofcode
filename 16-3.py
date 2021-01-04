f = [[int(y) for y in x.split()] for x in open('16-3.txt').read().split('\n')]

def valid(tr):
    for i in [0,1,2]:
        if tr[i]*2 >= sum(tr):
            return False
    return True

ct = 0
for i in f:
    if valid(i):
        ct += 1
print('part 1 -',ct)
ct = 0
for r in [0,1,2]:
 for i in range(int(len(f)/3)):
    tr = []
    for it in [0,1,2]:
       tr.append(f[i*3+it][r])    
    if valid(tr):
        ct += 1
print('part 2 -',ct)
