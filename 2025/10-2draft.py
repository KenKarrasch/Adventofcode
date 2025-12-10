
import numpy as np
f = open('ex.txt').read().split('\n')

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
    
def appjt(btn,jt,gm):
    nj = jt[:]
    for i in btn:
        nj[i] += 1
    return nj
            
def findp(i):
  #ltup = np.array([1, 2, 3, 4, 5])
  Q = [[[],[0]*len(lgts[i])]]
  dn = False    
  SEEN = []
  while Q and not dn:
    bl,jl = Q.pop(0)
    print('bl,jl',bl,jl)
    SEEN.append(jl)
    gd = True
    over = False
    for jt in range(len(jl)):
        if jl[jt] != nmss[i][jt]:
            gd = False
        if jl[jt] > nmss[i][jt]:
            over = True
    if gd:
        print(bl)
        return len(bl)
    if not over:
      for bt in btns[i]:
        if bt not in bl:
            njl = appjt(bt,jl,i)
            if njl not in SEEN:
                btl = bl+[bt]
                btl.sort()
                Q.append([btl,njl])
sm = 0
for i in range(len(lgts))[0:1]:
    #sm += findp(i)
    print(findp(i))

print(sm)
        




