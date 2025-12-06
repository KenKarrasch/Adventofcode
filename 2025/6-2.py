f = open('25-6.txt').read().split('\n')

#  6    5476   3626  ***

fs = []
op = []

for i in f[0:-1]:
    fs.append(i)

op = f[-1]

def getp(p):
    nm = 0
    fc = 1   
    nm = ''     
    for i in range(len(fs)):
        sn = fs[i][p]
        if sn != '0':
            nm = nm + sn    
    return(nm)


def add(s,e):
    sm = 0    
    for i in range(s,e-1):  
       sm += int(getp(i))
    return sm

def mult(s,e):
    sm = 1        
    for i in range(s,e-1):  
       sm *= int(getp(i))
    return sm

pl = []
for i in range(len(op)):    
    if op[i] in '+*':
        pl.append(i)
    

nfs = []
for i in range(len(fs)):
    ln = ''
    for j in range(len(fs[0])):
        if j+1 not in pl and fs[i][j] not in '0987654321':
            ln = ln + '0'
        else:
            ln = ln + fs[i][j]
    nfs.append(ln)

tly = 0
pl.append(len(fs[0])+1)
tk = range(len(pl)-1)

for i in tk:
    if op[pl[i]] == '+':
        tly += add(pl[i],pl[i+1])
    if op[pl[i]] == '*':
        tly += mult(pl[i],pl[i+1])
print(tly)
