f = open('15-9.txt').read().split('\n')
diss,c = [],[]

def getcities(m, c):
 for i in m:
   if len(i) > 0:
    g = i.split()
    if g[0] not in c:
     c.append(g[0])
    if g[2] not in c:
     c.append(g[2])
     
def finddests(f,st,been):
    d = []
    for u in f:
      s = u.split()[0] 
      e = u.split()[2] 
      if e not in been:
        if s == st:
         d.append(e)
      if s not in been:
        if e == st:
         d.append(s)
    return d
    
def getdist(s,e,f):
  for h in f:
    y = h.split()
    if y[0] in [s]:
      if y[2] in [e]:
        return int(y[4])
    if y[2] in [s]:
      if y[0] in [e]:
        return int(y[4])
    
def travel(s,been,f,depth,dist):
  if s not in been:
   if len(been) == depth - 1:
     diss.append(dist)
     return dist
   nbeen = been[:]
   nbeen.append(s)
   d = finddests(f,s,been)
   for p in d:
    ndist = getdist(s,p,f)
    ds = travel(p,nbeen,f,depth,ndist+dist)

getcities(f,c)
been = []
for s in c:
   t = travel(s,been,f,len(c),0)
print 'part 1 -',min(diss)
print 'part 2 -',max(diss)
