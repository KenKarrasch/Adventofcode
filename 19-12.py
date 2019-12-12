import re
from fractions import gcd

# The part 2 answer was 331 trillion, 331,346,071,640,472
# Had to search for rythms in orbits. 
# Do these for each axis separately, then 
# find the lowest common multiple LCM between the 3 axises rythm lengths.
# (This is the same as how real 
# planetary orbit transits are calculated)
# Caution: be careful with the lcm algorithm used.
# some are n squared, which are very slow.

inp = open('19-12.txt').read()
w = [int(d) for d in re.findall(r'[+-]?[0-9]+',inp)]

p,v,ct = [],[[0 for i in range(3)] for h in range(len(w)/3)],0

while ct < len(w):
   pl = []
   for i in range(3):
     pl.append(w[ct])
     ct += 1
   p.append(pl)

def getd(d,j,gp):
  if j > gp: return 1
  if gp > j: return -1
  if gp == j: return 0

def getv(v,gp,p):
  nv = v[:]
  for j in p:
   if j != gp:
    for d in [0,1,2]:
     nv[d] += getd(d,j[d],gp[d])
  return nv
  
def uv(p,v):
   nv = [[j for j in g] for g in v]
   for pl in range(len(p)):
     nv[pl] = getv(v[pl],p[pl],p)
   return nv
   
def up(p,v):
   np = [[j for j in g] for g in p]
   for pl in range(len(p)):
     for d in [0,1,2]:
       np[pl][d] += v[pl][d]
   return np
   
xs,ys,zs = [],[],[]
cy = [0,0,0]
for u in range(300000):
    if u%50000 == 0:
     print u
    nv = uv(p,v)
    np = up(p,nv)
    p = [[j for j in g] for g in np]
    v = [[j for j in g] for g in nv]
    hx,hy,hz= [],[],[]
    for x in p:
      hx.append(x[0])
      hy.append(x[1])
      hz.append(x[2])
    for x in v:
      hx.append(x[0])
      hy.append(x[1])
      hz.append(x[2])
    if u == 0:
      xs.append(hx)
      ys.append(hy)
      zs.append(hz)
    if hx in xs:
        if cy[0] == 0:
          cy[0] = u
    if hy in ys:
        if cy[1] == 0:
          cy[1] = u
    if hz in zs:
        if cy[2] == 0:
          cy[2] = u
    if u == 1000:
     tp = []
     for y in p:
      am = 0
      for j in y:
       am += abs(j)
      tp.append(am)
     tv = []
     for y in v:
      am = 0
      for j in y:
       am += abs(j)
      tv.append(am)
     tot = 0
     for a in range(len(p)):
      tot += tv[a]*tp[a]
     print 'part 1 -', tot

def flcm(a, b):
    return a * b // gcd(a, b)

st = flcm(cy[0],cy[1])
print 'part 2 -',flcm(cy[2],st)
