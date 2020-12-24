import copy

# runs fast on pypy, slow on Python 3
# combo puzzle, pt1 navigation and pt2 game of life.

file = '20-24.txt'
f = open(file).read().split('\n')

m = ['se','sw','ne','nw','w','e']
mv = [[1,-1],[-1,-1],[1,1],[-1,1],[-2,0],[2,0]]

sz = 100 + 2*max([len(x) for x in f])
gr = [[1 for x in range(2*sz)] for y in range(2*sz)]
adj = [[-2,0],[-1,1],[1,1],[2,0],[1,-1],[-1,-1]]

mvs,drs = [],[]
for j in f:
    i = 0
    while i < len(j):
        if j[i:i+2] in m[0:4]:        
            drs.append(j[i:i+2])            
            i += 2
        else:
            drs.append(j[i])
            i += 1
    mvs.append(drs[:])
    drs = []
ct = 0
for i in mvs:
    x,y  = 0,0
    for j in i:
        for s in range(len(m)):
            if j == m[s]:
                 x += mv[s][0]
                 y += mv[s][1]
    if gr[x+sz][y+sz] == 1:
        gr[x+sz][y+sz] = 0
        ct += 1
    else:
        gr[x+sz][y+sz] = 1
        ct -= 1
print('part 1 -',ct)
ngr = copy.deepcopy(gr)
for k in range(100):
  for x in range(2,(sz*2)-2):
    for y in range(2,(sz*2)-2):      
        ct = 0
        for a in adj:          
            if not gr[x+a[0]][y+a[1]]:
                ct += 1
        if not gr[x][y]: # 0 is Black, 1 is White           
            if (ct>2) or (ct==0):
                ngr[x][y] = 1
        else:
            if ct == 2:
                ngr[x][y] = 0
  gr = copy.deepcopy(ngr)
  ct = 0
  for x in range(sz*2):
    for y in range(sz*2):
        if gr[x][y] == 0:
            ct += 1
print('part 2 -',ct)
