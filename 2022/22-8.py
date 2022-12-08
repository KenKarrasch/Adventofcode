f = open('22-8.txt').read().split('\n')

g = []

for i in f:
    ln = []
    for c in i:
        ln.append(int(c))
    g.append(ln)
    
drs = [[1,0],[-1,0],[0,1],[0,-1]]
    
def st(x,y,ht):
    if g[x][y] < ht:
        return True
    return False
    
def sf(x,y):
    if len(g) > x >= 0:
      if len(g) > y >= 0:
         return True
    return False
    
def sch(x,y):
    ht = g[x][y]
    for d in drs:
      nx,ny = x,y
      nx += d[0]
      ny += d[1]
      done = False
      while not done:
        if sf(nx,ny):
          if not st(nx,ny,ht):
            done = True
        else: 
          return True
        nx += d[0]
        ny += d[1]
    return False
    
def scc(x,y):
    nx,ny = x,y
    ht = g[x][y]
    ed = False
    scs = []
    for d in drs:
      nx,ny = x,y
      nx += d[0]
      ny += d[1]
      done = False
      ls = 0
      while not done:
        ls += 1
        if sf(nx,ny):
          if not st(nx,ny,ht):
            done = True
            scs.append(ls)
        else: 
          done = True
          scs.append(ls-1)
        nx += d[0]
        ny += d[1]
    return scs

t = 0
for x in range(len(g)):
  for y in range(len(g)):
    if sch(x,y):
      t += 1
      
print 'part 1 -',t
        
sccs = []
for x in range(len(g)):
  for y in range(len(g)):
    sccs.append(scc(x,y))

scss = []
for i in sccs:
    sc = 1
    for j in i:
      if j != 0:
        sc = sc*j
    scss.append(sc)
print 'part 2 -',max(scss)
