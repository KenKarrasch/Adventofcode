r = open('19-18.txt').read().split('\n')

# To solve this I needed to the use of BFS, Dijkstra shortest path algoritm, and
# help of caching to prevent reworking the same path over again.

# step 1, convert puzzle into web by looking for nodes and letters.
# step 2, work out the distance between nodes and letters using BFS, create
#         library with this information.
# step 3, Do recursive algoritm, looking at the various options where the
#         robot can go at each recursion. Usually there is between 2 and 5
#         places to go. There will be about 2.5^52 branches = 5e+20,
#        (...so do step 4)
# step 4, implement caching algorithm, at each branch node, store off the
#         quickest way to an end. Other Branches will find this useful as they
#         often have identical routes.

# Caching saved a tonne of time.  317,369 caching nodes created, 993,482 cache hits.

# Unsure, how much faster caching is but it is aleast 50 times, I tried testing
# a smaller puzzle but gave up waiting.

# Takes 1min 25s

g = [[0 for b in a] for a in r]

for x in range(len(r)): 
 for y in range(len(r[x])):
   g[x][y] = r[x][y]
   if g[x][y] == '@':
     rob = (x,y)

def printmn(g,nodes):
 for a in range(len(g)):
  ln = ''
  for b in range(len(g[a])):
    if (a,b) in nodes:
      ln += '@'
    else: ln += g[a][b]    
  print(ln)

def getnodes(g):
 node = {}
 num = 0
 d = [[0,1],[1,0],[0,-1],[-1,0]]
 for x in range(1,len(g)-1): 
  for y in range(1,len(g[x])-1):
   if (g[x][y] == '.') or (g[x][y] == '@'):
    n = 0
    for a in d:
     if g[x+a[0]][y+a[1]] == '#':        
      n += 1
    if n < 2:
     node[(x,y)] = num
     num += 1
 return node

d = [[0,1],[1,0],[0,-1],[-1,0]]
adds = True
while adds:
 adds = False
 for x in range(1,len(g)-1): 
  for y in range(1,len(g[x])-1):
   if g[x][y] == '.':
    n = 0
    for a in d:
     if g[x+a[0]][y+a[1]] == '#':        
      n += 1
    if n == 3:
     g[x][y] = '#'
     adds = True

def findopts(rob,gop,doorsopen,keysfd,nodes,uc,lc,dist):
   options = []
   go = []
   distl = []
   for a in gop[rob]:
    go.append(a)
    distl.append(gop[rob][a]+dist)
   i = 0
   while i < len(go):
     np = go[i]     
     crawl = False
     if (np in uc) and (np in doorsopen): # door open already
      crawl = True          
     if (np in lc) and (np in keysfd): # got key already
      crawl = True
     if np in nodes: # this is a node, keep going
      crawl = True
     if (np in lc) and not (np in keysfd): # new key, add as an option
      options.append([distl[i],lc[np],np])    
     if np in uc: # door, got key, add as an option
      if chr((ord(uc[np])+32)) in keysfd.values():
        if np not in doorsopen:
         options.append([distl[i],uc[np],np])
     if crawl:
      for a in gop[np]:
        if a not in go:
         go.append(a)
         distl.append(gop[np][a]+distl[i])
     i += 1     
   return options    

def getp(g):
 bl = {}
 for x in range(1,len(g)-1): 
  for y in range(1,len(g[x])-1):
   if (g[x][y] == '.') or (g[x][y] == '@'):
    bl[(x,y)] = True
   if g[x][y] in 'qwertyuiopasdfghjklzxcvbnm':
    lc[(x,y)] = g[x][y]
   if g[x][y] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    uc[(x,y)] = g[x][y]    
 return bl,uc,lc

def explore(rob,gop,doorsopen,keysfd,dist,score,depth,nodes,uc,lc):
  global best
  global cache
  hsh = gethash(rob,doorsopen,keysfd)
  if hsh in cache:
    return cache[hsh]+dist # already beed down this path, return the previous result
  if (len(keysfd) == len(lc)):
    score.append(dist)        
    if dist < best:
      best = dist
    return dist
  options = findopts(rob,gop,doorsopen,keysfd,nodes,uc,lc,dist)
  bestjmp = [100000000]
  for opt in options:
    if opt[0] < best: # path is already longer prev best, no need to explore any further
      nkeysfd = keysfd.copy()
      ndoorsopen = doorsopen.copy()    
      if opt[2] in uc:          
        ndoorsopen[opt[2]] = opt[1]        
      if opt[2] in lc:        
        nkeysfd[opt[2]] = opt[1]
      if (opt[2] in lc) or (opt[2] in uc):
        r = (opt[2][0],opt[2][1])
        bestjmp.append(explore(r,gop,ndoorsopen,nkeysfd,opt[0],score,depth+1,nodes,uc,lc))    
        
  if hsh in cache:
    if cache[hsh] > min(bestjmp)-dist:
       cache[hsh] = min(bestjmp)-dist
  else:      
    cache[hsh] = min(bestjmp)-dist
  if depth < 1:
    print(cache[hsh])
  return min(bestjmp)

def gethash(rob,doorsopen,keysfd):  
  hsh = str(rob)
  keys,doors = [],[]  
  for a in keysfd.values():
    keys.append(a)
  keys.sort()
  for a in doorsopen.values():
    doors.append(a)
  doors.sort()
  for ch in keys:
     hsh += ch
  for ch in doors:
     hsh += ch
  return hsh

def findlks(rob,bl,nodes,uc,lc):
   t = {rob:0}
   d = [[0,1],[1,0],[0,-1],[-1,0]]
   dp,mv = 1, True   
   options = {}
   while mv:
    crop = []
    mv = False
    for r in t:
     if t[r] == dp-1:
      for a in d:       
       np = (r[0]+a[0], r[1]+a[1])
       if np not in t:
        if (np in bl) and \
           not (np in uc) and \
           not (np in lc) and \
           not (np in nodes):           
          crop.append(np)
        if (np in nodes):
          options[np] = dp
        if (np in lc):
          options[np] = dp
        if (np in uc):
          options[np] = dp        
    for a in crop:
      mv = True
      t[a] = dp
    dp += 1
   return options
    
nodes = getnodes(g)  
printmn(g,nodes)
bl,uc,lc = {},{},{}
bl,uc,lc = getp(g)
cache,gop = {},{}
gop[rob] = findlks(rob,bl,nodes,uc,lc)
for a in nodes:
  gop[a] = findlks(a,bl,nodes,uc,lc)
for a in uc:
  gop[a] = findlks(a,bl,nodes,uc,lc)
for a in lc:
  gop[a] = findlks(a,bl,nodes,uc,lc)
doorsopen,keysfd = {},{}

best = 1000000
s = explore(rob,gop,doorsopen,keysfd,0,[],0,nodes,uc,lc)
