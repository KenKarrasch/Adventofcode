import copy
# straightforward multidimensional puzzle
f = open('20-17b.txt').read().split('\n')

cs = 6
gw = len(f[0]) + 2*cs
gr = range(gw)

g = [[['.' for x in gr] for y in gr] for z in gr]

for i in range(len(f)):
    for w in range(len(f)):
        g[9][i+cs][w+cs] = f[i][w]

def cc(x,y,z,v,w,u):
    if(gw>x+v>=0):
       if(gw>y+w>=0):
         if(gw>z+u>=0):
            if g[x+v][y+w][z+u] == '#':
                if (v!=0) or (u!=0) or (w!=0):
                    return 1
    return 0

for cy in range(6):
    
  ngw = [x[:] for x in g]
  ngw = copy.deepcopy(g)

  for x in gr:
    for y in gr:
      for z in gr:
        ct = 0
        for v in [-1,0,1]:
         for w in [-1,0,1]:
          for u in [-1,0,1]:
           ct += cc(x,y,z,v,w,u)
        if g[x][y][z] == '#':
           if ct not in [2,3]:
            ngw[x][y][z] = '.'
        if g[x][y][z] == '.':
           if ct in [3]:
            ngw[x][y][z] = '#'
  g = copy.deepcopy(ngw)


ct = 0
for x in gr:
   for y in gr:
     for z in gr:
         if g[x][y][z] == '#':
             ct += 1
print 'part 1 -',ct

g = [[[['.' for x in gr] for y in gr] for z in gr] for zz in gr]

for i in range(len(f)):
    for w in range(len(f)):
        g[9][9][i+cs][w+cs] = f[i][w]

def cc2(x,y,z,zz,v,w,u,uu):
    if(gw>x+v>=0):
       if(gw>y+w>=0):
         if(gw>z+u>=0):
           if(gw>zz+uu>=0):
            if g[x+v][y+w][z+u][zz+uu]== '#':
                if (v!=0) or (u!=0) or (w!=0) or (uu!=0):
                    return 1
    return 0

for cy in range(6):
  ngw = copy.deepcopy(g)
  for x in gr:
    for y in gr:
      for z in gr:
       for zz in gr:
        ct = 0
        for v in [-1,0,1]:
         for w in [-1,0,1]:
          for u in [-1,0,1]:
           for uu in [-1,0,1]:
            ct += cc2(x,y,z,zz,v,w,u,uu)
        if g[x][y][z][zz] == '#':
           if ct not in [2,3]:
            ngw[x][y][z][zz] = '.'
        if g[x][y][z][zz] == '.':
           if ct in [3]:
            ngw[x][y][z][zz] = '#'
  g = copy.deepcopy(ngw)

ct = 0
for x in gr:
   for y in gr:
     for z in gr:
       for zz in gr:
         if g[x][y][z][zz] == '#':
             ct += 1
print 'part 2 -',ct
