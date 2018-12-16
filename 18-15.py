G = 0
E = 1
size = 0

def gobsdead(unit):
  for g in unit:
    if g[3] == G:      
      return False
  return True
      
def elsdead(unit):
  for g in unit:
    if g[3] == E:      
      return False
  return True

def printunits(unit,wall,size):  
  for y in range(size):
    strs = ''
    health = ''    
    for x in range(size):
      ch = '.'
      for u in unit:
        if u[0] == y and u[1] == x:
          if u[3] == G:
            ch = 'G'            
          if u[3] == E:
            ch = 'E'        
          health = health + ch + '(' + str(u[2]) +')'
      for w in wall:
        if w[0] == y and w[1] == x:
          ch = '#'
      strs += ch
    print strs, health

def nextto(a,b):
    if a[0] == b[0]:
      if a[1] == b[1] + 1 or a[1] == b[1] - 1:
        return True
    if a[1] == b[1]:
      if a[0] == b[0] + 1 or a[0] == b[0] - 1:
        return True
    return False

def findunitsinrange(units,wall,u):
  if units[u][3] == G:
    enemy = E
  else: enemy = G
  enemies = []
  inrange = []
  for e in range(len(units)):
      if units[e][3] == enemy:
        enemies.append([units[e][0], units[e][1]])
  for y in range(size):
    for x in range(size):
      free = False
      for e in enemies:
        if nextto([e[0],e[1]],[y,x]):          
          free = True
      for e in units: # No other unit sitting there already
        if e[0] == y and e[1] == x:
          free = False
      for w in wall: # not a wall
        if w[0] == y and w[1] == x:
          free = False
      if free:         
        inrange.append([y,x])
  return inrange

def printdmap(dmap):
  for y in dmap:
    print y
      
def reachable(r, dmap, depth):
  dupmap = []
  for l in dmap:
    dl = l[:]
    dupmap.append(dl)
  keepsearching = False
  found = False
  for y in range(size):    
    for x in range(size):      
      if dupmap[y][x] == depth:
        if nextto(r,[y,x]):
          found = True
        if y < size - 1:
          if dupmap[y+1][x] == 0:
           dupmap[y+1][x] = depth + 1
           keepsearching = True
        if y > 0:
          if dupmap[y-1][x] == 0:
           dupmap[y-1][x] = depth + 1
           keepsearching = True
        if x < size - 1:
          if dupmap[y][x+1] == 0:
           dupmap[y][x+1] = depth + 1
           keepsearching = True
        if x > 0:
          if dupmap[y][x-1] == 0:
           dupmap[y][x-1] = depth + 1
           keepsearching = True
  if found:
    return [depth, dupmap]
  if not keepsearching:
    return [-1, []]
  return reachable(r, dupmap, depth + 1)
   
      
def findreachable(unit,wall,u,findrange):
   # breadth first search
   reachableunit = []
   rmap = [[0 for q in range(size) ] for w in range(size)]        
   for y in range(size):    
    for x in range(size):
      ch = 0                
      for i in unit:
        if i[0] == y and i[1] == x:
          if i[3] == 'G':
            ch = -1
          if i[3] == 'E':
            ch = -1
   for i in unit:     
     rmap[i[0]][i[1]] = -1
   for w in wall:
     rmap[w[0]][w[1]] = -1
   rmap[unit[u][0]][unit[u][1]] = 1
   for r in findrange:    
     dist = reachable(r,rmap,1)
     if dist[0] > -1:
       reachableunit.append([dist[0], r[0], r[1], dist[1]])       
   reachableunit.sort(key=lambda i: tuple(i[:3]))
   if len(reachableunit) > 0:
     best = reachableunit[0]
     if len(best) > 0:
       return best
   return []
  
def inrange(unit, u):
  targets = []
  for p in range(len(unit)):
    if nextto(unit[u][:2], unit[p][:2]) and unit[u][3] != unit[p][3]:
      targets.append([unit[p][2],unit[p][0],unit[p][1],p])
  return targets

def moveto(current, end, dupmap, path, depth):
      newpath = []      
      for ps in path:
        newpath.append(ps)
      newpath.append(current)
      if current == end:
         return [True, newpath]
      returnpath = []
      found = False
      if current[0] > 0:
        if dupmap[current[0]-1][current[1]] == depth+1:            
          returnpath = moveto([current[0]-1,current[1]],end,dupmap,newpath,depth+1)
          if returnpath[0]:
            return returnpath
      if current[1] > 0:
        if dupmap[current[0]][current[1]-1] == depth+1:            
          returnpath = moveto([current[0],current[1]-1],end,dupmap,newpath,depth+1)
          if returnpath[0]:
            return returnpath
      if current[1] < size - 1:
        if dupmap[current[0]][current[1]+1] == depth+1:            
          returnpath = moveto([current[0],current[1]+1],end,dupmap,newpath,depth+1)           
          if returnpath[0]:
            return returnpath
      if current[0] < size - 1:
        if dupmap[current[0]+1][current[1]] == depth+1:            
          returnpath = moveto([current[0]+1,current[1]],end,dupmap,newpath,depth+1)           
          if returnpath[0]:
            return returnpath
      return [False, returnpath]

def countelves(unit):
  count = 0
  for h in unit:
    if h[3] == E:
      count += 1
  return count
      
tr = open('18-15-2.txt','r').read().split('\n')
unit = []
el = []
wall = []


for y in range(len(tr)):  
  for x in range(len(tr[y])):
    if tr[y][x] == 'G':
      unit.append([y,x,200,G,True])
    if tr[y][x] == 'E':
      unit.append([y,x,200,E,True])
    if tr[y][x] == '#':    
      wall.append([y,x])

unitcopy = []
wallcopy = []
for y in unit:
  unitcopy.append(y[:])
for z in wall:
  wallcopy.append(z[:])
  
size = len(tr)
printunits(unit,wall,size)

c = 0
g = 0
elveswon = False
elhp = 3
elnum = countelves(unit)
print 'elnum', elnum 
while not elveswon:
  unit = []
  wall = []
  for y in unitcopy:
    unit.append(y[:])
  for z in wallcopy:
    wall.append(z[:])
  c = 0
  print '******** elves hp *********',elhp
  finished = False
  while not gobsdead(unit) and not elsdead(unit) and not finished:
    c += 1    
    if elhp == 34:
      print '==========New Round============',c
    unit.sort(key=lambda i: tuple(i[:2]))
    u = 0
    targets = []
    while u < len(unit):
       targets = inrange(unit,u)
       targets.sort(key=lambda i: tuple(i[:3]))
       if len(targets) == 0:
        findrange = findunitsinrange(unit,wall,u)
        reachableunit = findreachable(unit,wall,u,findrange)
        nspot = []
        if len(reachableunit) > 0:
          nspot.append(moveto(unit[u][:2], reachableunit[1:3], reachableunit[3],[],1)[1])
        if len(nspot) > 0:
          unit[u][0] = nspot[0][1][0]
          unit[u][1] = nspot[0][1][1]
       targets = []
       targets = inrange(unit,u)
       targets.sort(key=lambda i: tuple(i[:3]))
       if len(targets) > 0:
        uinrange = targets[0][3]
        if uinrange != -1:
          if unit[u][3] == E:            
            unit[uinrange][2] -= elhp
          else:
            unit[uinrange][2] -= 3
          if unit[uinrange][2] < 1:
            unit.pop(uinrange)
            if gobsdead(unit) and u != len(unit):
                c -= 1
                finished = True              
            if u > uinrange:
              u -= 1
       u += 1  
    u = 0
    finished = False     
  printunits(unit,wall,size)
    
  tp = 0
  for u in unit:
    tp += u[2]
  if elhp == 3:
    print 'part 1 -', tp*(c)
  if countelves(unit) == elnum:
    print 'part 2 -', tp*(c)
    elveswon = True
  elhp += 1
  g += 1
        
