import numpy as np
f = open('in.txt').read().split('\n')
# 10    2065   4898  ***

lgts = []
btns = []
nmss = []

for dt in f:
    lgt = [x for x in dt.split(']')[0].split('[')[1]]
    bt = dt.split(']')[1].split('{')[0].split()
    bt1 = [x.replace(')','').replace('(','') for x in bt]
    bts = [[int(y) for y in x.split(',')] for x in bt1]
    nms = [int(y) for y in dt.split('{')[1].split('}')[0].split(',')]
    lgts.append(lgt)
    btns.append(bts)
    nmss.append(nms)

def appbt(btn,l,gm):
    nl = l[:]
    for i in btn:
        if nl[i] == '#':
            nl[i] = '.'
        else:
            nl[i] = '#'
    return nl
            
def findp(i):
  #ltup = np.array([1, 2, 3, 4, 5])
  Q = [[[],['.']*len(lgts[i])]]
  dn = False    
  SEEN = []
  while Q and not dn:
    bl,l = Q.pop(0)
    SEEN.append(l[:])
    gd = True
    for lg in range(len(l)):
        if l[lg] != lgts[i][lg]:
            gd = False
    if gd:
        return len(bl)
    for bt in btns[i]:
        if bt not in bl:
            nl = appbt(bt,l,i)
            if nl not in SEEN:
                Q.append([bl+[bt],nl])
sm = 0
for i in range(len(lgts))[0:10]:
    sm += findp(i)

print(sm)
