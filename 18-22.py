f = open('18-22.txt').read().split('\n')
# Used a breadth first search (Dijkstra), i.e. iteratively at each second populate a
# map of where we 'could' be located in the cave.  If we reach a place that we have been
# before terminate that line. Do this until the destination is found.
# The mistake that costed me alot of time was that when changing equipment, the new
# equipment must be satisfactory for both the start and destination squares, not just
# the destination, as I had assumed.
# This solution should work for all cases.  This solution could be done using recursion.

CLIMB, TORCH, NEITHER = 0,1,2
ROCKY, WET, NARROW = 0,1,2
sw = 7 + 1 #switchtime
depth = int(f[0].split()[1])
target = int(f[1].split()[1].split(',')[0]), \
         int(f[1].split()[1].split(',')[1])
sz = max(target) + 50
inf = 2*max(target)
ero = [[0 for i in range(sz)] for j in range(sz)]
flt = [[inf for i in range(sz)] for j in range(sz)]
flc = [[inf for i in range(sz)] for j in range(sz)]
fln = [[inf for i in range(sz)] for j in range(sz)]
flt[0][0] = 0
ero[0][0] = ((0 + depth) % 20183) % 3
for i in range(sz):
  ero[i][0] = ((i * 16807 + depth) % 20183)
for j in range(sz):
  ero[0][j] = ((j * 48271 + depth) % 20183)
for i in range(1,sz):
  for j in range(1,sz):
    ero[i][j] = ((ero[i-1][j]*ero[i][j-1] + depth) % 20183)
    if i == target[0] and j == target[1]:
        ero[i][j] = ((0 + depth) % 20183)
risklevel = 0
for i in range(target[0]+1):
  for j in range(target[1]+1):
    risklevel += ero[i][j] % 3
print 'part 1 -', risklevel

def getplacesattime(time):
    places = []
    for i in range(sz):
      for j in range(sz):
          if flc[i][j] == time:
              places.append([i,j,[True,False]])  #CLIMB            
          if flt[i][j] == time:
              places.append([i,j,[False,True]])  #TORCH
          if fln[i][j] == time: 
              places.append([i,j,[False,False]]) #NEITHER         
    return places[:]

def opp(eq,pl):
  t = ero[pl[0]][pl[1]] % 3
  if eq == [False,False]:#NEITHER:
    if t == WET:
      return [True,False]#CLIMB
    if t == NARROW:
      return [False,True]#TORCH
  if eq == [True,False]:#CLIMB:
    if t == ROCKY:
      return [False,True]#TORCH
    if t == WET:
      return [False,False]#NEITHER
  if eq == [False,True]:#TORCH:
    if t == ROCKY:
      return [True,False]#CLIMB
    if t == NARROW:
      return [False,False]#NEITHER
    
def move(x,y,tool,time):   
   if x > -1 and y > -1 and x < sz and y < sz:
     besttime = [inf,inf,inf]                     
     if ero[x][y] % 3 == ROCKY:
        besttime[NEITHER] = inf                        
        if tool[TORCH]:
            besttime[TORCH] = time
        if tool[CLIMB]:
            besttime[CLIMB] = time
     if ero[x][y] % 3 == WET:
        besttime[TORCH] = inf
        if tool[CLIMB]:
            besttime[CLIMB] = time
        if not tool[CLIMB] and not tool[TORCH]:            
            besttime[NEITHER] = time
     if ero[x][y] % 3 == NARROW:
        besttime[CLIMB] = inf                 
        if tool[TORCH]:        
            besttime[TORCH] = time
        if not tool[CLIMB] and not tool[TORCH]:
            besttime[NEITHER] = time
     if x == target[0] and y == target[1]:
        besttime[CLIMB] = inf
        besttime[NEITHER] = inf
        if tool[TORCH]:        
            besttime[TORCH] = time
     if besttime[NEITHER] < fln[x][y]:
           fln[x][y] = besttime[NEITHER];
     if besttime[CLIMB] < flc[x][y]:
           flc[x][y] = besttime[CLIMB];  
     if besttime[TORCH] < flt[x][y]:
           flt[x][y] = besttime[TORCH];
                            
reachedtarget = False
tool = [True, False]
time = 0
places = []
maxp = 0
while not reachedtarget:
   places = getplacesattime(time)   
   for pl in places:
     # Breadth first search
     if maxp < pl[1] - 9:
       print 'searching :- up to line',maxp, 'of', max(target)
       maxp = pl[1]   
     move(pl[0]+1,pl[1],pl[2],time+1)
     move(pl[0]-1,pl[1],pl[2],time+1)
     move(pl[0],pl[1]+1,pl[2],time+1)
     move(pl[0],pl[1]-1,pl[2],time+1)
     #try changing equipment
     move(pl[0]+1,pl[1],opp(pl[2],pl),time+sw)
     move(pl[0]-1,pl[1],opp(pl[2],pl),time+sw)
     move(pl[0],pl[1]+1,opp(pl[2],pl),time+sw)
     move(pl[0],pl[1]-1,opp(pl[2],pl),time+sw)     
   if flt[target[0]][target[1]] == time:
       print 'part 2 -',time
       reachedtarget = True
   time += 1   
