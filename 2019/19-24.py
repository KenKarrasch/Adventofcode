rb = open('19-24.txt').read().split('\n')
# Rank 679/587
# Fairly straightforward puzzle, probably designed for the kids,
# good one for doing after work.  Learning for me - exception handling.

r = []
sz = [0,1,2,3,4]

for a in sz:
    ln = []
    for b in sz:      
      if rb[a][b] == '#':
          ch = 1
      else: ch = 0
      ln.append(ch)
    r.append(ln)
    
def printg(r):
    for a in sz:
       ln = ''
       for b in sz:
           if r[a][b] == 1:
              ln += '#'
           else:
              ln += '.'
       print(ln)

def geth(x,y,r):
  if (x > -1) and (x < 5) and (y > -1) and (y < 5):
    return r[x][y]
  else: return 0

def gethb(x,y,bgs,b,fx,fy):
  if (b < 0) or (b > len(bgs)-2):
      return 0  
  if x == -1:
     if bgs[b-1][1][2] == 1:
        return 1
     return 0
  if x == 5:
     if bgs[b-1][3][2] == 1:
        return 1
     return 0
  if y == -1:
     if bgs[b-1][2][1] == 1:
        return 1
     return 0
  if y == 5:
     if bgs[b-1][2][3] == 1:
        return 1
     return 0
  if (x == 2) and (y == 2):
    t = 0
    for a in [0,1,2,3,4]:
     if fx == 3:
       t += bgs[b+1][4][a]     
     if fx == 1:     
       t += bgs[b+1][0][a] 
     if fy == 3:     
       t += bgs[b+1][a][4] 
     if fy == 1:     
       t += bgs[b+1][a][0] 
    return t
  try:
    return bgs[b][x][y]
  except:
    print(b,x,y)

     
d = [[0,1],[1,0],[0,-1],[-1,0]]
br = [b[:] for b in r]
bgs = []
bgs.append(br)
dup = False
while not dup:
 nr = [b[:] for b in r]
 for x in sz:
  for y in sz:
     adj = 0
     for ad in d:        
        if geth(x+ad[0],y+ad[1],r):
          adj += 1
     if r[x][y] == 1:
        if adj == 1:
          nr[x][y] = 1
        else: nr[x][y] = 0            
     if r[x][y] == 0:
        if (adj == 1) or (adj == 2):
          nr[x][y] = 1
 ad = [b[:] for b in nr]
 for a in bgs:
  bad = False
  for x in sz:
    for y in sz:
      if a[x][y] != ad[x][y]:
        bad = True
  if bad == False:
    dup = True
    tot = 0
    for x in sz:
      for y in sz:
        if ad[x][y] == 1:
          num = 5*x + y
          tot += 2**num
    print('part 1 -',tot)
    done = True
 bgs.append([b[:] for b in nr])
 r = [b[:] for b in nr]

r = []
for a in sz:
    ln = []
    for b in sz:      
      if rb[a][b] == '#':
          ch = 1
      else: ch = 0
      ln.append(ch)
    r.append(ln)
    
br = [b[:] for b in r]
nr = []
bgs = []
ms = 200
mms = (2*ms) + 1
for a in range(mms):
    bgs.append([[0,0,0,0,0] for b in [0,1,2,3,4]])
for x in sz:
  for y in sz:
    bgs[ms][x][y] = br[x][y]
for n in range(200):
 nbgs = []
 for i in range(len(bgs)):
   nr = []
   nr = [b[:] for b in bgs[i]]
   nbgs.append([a[:] for a in nr])
 for b in range(mms):
   for x in sz:
    for y in sz:     
     adj = 0        
     for ad in d:        
          adj += gethb(x+ad[0],y+ad[1],bgs,b,x,y)   
     if (x != 2) or (y != 2):
      if bgs[b][x][y] == 1:
        if adj == 1:
          nbgs[b][x][y] = 1
        else: nbgs[b][x][y] = 0            
      if bgs[b][x][y] == 0:
        if (adj == 1) or (adj == 2):
          nbgs[b][x][y] = 1
     else: nbgs[b][x][y] = 0
 bgs = []
 for i in range(len(nbgs)):
   nr = [b[:] for b in nbgs[i]]
   bgs.append(nr)

ct = 0
for a in range(len(bgs)):
  for x in sz:
      for y in sz:
        ct += bgs[a][x][y]

print('part 2 -',ct)
