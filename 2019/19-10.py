import math as mt
#Did the first part using integers and logic.
#That strategy did not work for part 2
#ended up using polar coordinates.
#Made the mistake of adding
#pi instead of 2pi to get positive phi's.
#Then the floating point accuracy issues came into 
#play so had to fudge a tiny bit

w = open('19-10.txt').read().split('\n')

m = []
for g in w:
    t = []
    for o in g:
      if o == '#':
        t.append(1)
      else:
        t.append(0)
    m.append(t)
szx = len(m)
szy = len(m[0])

def bl(h,j):
   if h > -1:
    if j > -1:
      if h < szx:
        if j < szy:
          return(True)
   return(False)
        
def hcf(x, y):
  hcfo = 1
  if x > y:
    smaller = y
  else:
    smaller = x
  for i in range(1, smaller+1):
   if((x%i == 0) and (y%i == 0)):
        hcfo = i 
  return hcfo

def ls(x,y):
  n = []
  for g in m:
    n.append(g[:])
  for u in range(len(m)):
   for v in range(len(m[u])):
     dv = y-v
     du = x-u
     if (dv!=0) or (du!=0):
      if dv == 0:
        duh = du/abs(du)
        dvh = 0
      if du == 0:
        dvh = dv/abs(dv)
        duh = 0
      if du and dv:
        dvh = dv/hcf(abs(dv),abs(du))
        duh = du/hcf(abs(dv),abs(du))
      if m[u][v] == 1:
        for ds in range(szx):
          d = ds + 1
          dsx = du
          dsy = dv
          if bl(x-(dsx+d*duh),y-(dsy+d*dvh)):
            n[x-(dsx+d*duh)][y-(dsy+d*dvh)] = 0
      
  ast = 0
  for k in range(len(n)):
    for l in range(len(n[k])):
     if n[k][l] == 1:
        ast += 1
  return ast-1
  
res = []
cd = []

for x in range(len(m)):
  for y in range(len(m[x])):
     if m[x][y] == 1:
        res.append(ls(x,y))
        cd.append([x,y])
     else:
        res.append(0)
        cd.append([x,y])
best = max(res)
bc = []
for ind in range(len(res)):
  if res[ind] == best:
      print 'part 1 -',best
      bc = cd[ind][:]

def c2p(x,y,u,v):
    rho = mt.sqrt(x**2 + y**2)
    phi = mt.atan2(y, x)
    if phi < -0.000005:
        phi += 2*mt.pi
    return([rho, phi,u,v])

c = []
for g in m:
    c.append(g[:])
x,y = bc[0],bc[1]
crd = []

for u in range(len(m)):
  for v in range(len(m[u])):
    if m[u][v] == 1:
       pl = c2p(x-u,v-y,v,u)
       if x-u!=0 or v-y!=0:
         crd.append(pl)
       
crd = sorted(crd, key = lambda x: (x[1], x[0]))
       
for h in range(len(m)):
  st = []
  for ch in range(len(m[h])):
    if h == bc[0] and ch == bc[1]:
        st.append(str(2))
    else:
      st.append(str(m[h][ch]))

hit = []

for y in crd:
  hit.append(False)
  
def findclosest(crd,lr,hit):
  ang = []
  for h in range(len(crd)):
   if not hit[h]:
    if crd[lr][1] > crd[h][1]-0.00000005 and crd[lr][1] < crd[h][1]+0.00000005:
       ang.append([h,crd[h][0]])
  ang = sorted(ang, key = lambda x:         (x[1], x[0]))
  return ang[0][0]
  
def findnext(crd,lr,hit):
    ang = crd[lr][1]
    for h in range(len(crd)):
      if crd[h][1] > ang+0.00000005:
        return h

lr = 0
ct = 1
depth = 201
for j in range(depth-1):
   lr = findclosest(crd,lr,hit)
   hit[lr] = True
   if ct == 200:
     print 'part 2 -',crd[lr][2]*100+crd[lr][3]
   ct += 1
   lr = findnext(crd,lr,hit)
