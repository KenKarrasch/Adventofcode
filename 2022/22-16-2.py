f = open('22-16.txt').read().split('\n')

# Part 1 - 
#  Start by getting the distances between valves this non zero flow rates, use BFS.
#  Then recursively search these nodes to find the best route.

# Part 2 - 
#  set timer to 26 mins.
#
#  New Version - the previous version assumed the best single solution will be part of the best combined solution (part 2), which
#  worked for my input but not others.  This is a general solution with finds the best pair combined.
#
#  solution :-
#
#  search algorithm from part one stores every possible solution and the flow amount for each possibility
#
#  Set up a set, for each valve that can open, form a list of paths that didn't visit them.
#
#  Look at each path, then using set intersection work out which paths did not visit the same valves.
#  keep track of best total
#  
#  Takes about 10min, may want to put on a cup of tea while waiting.

# Part 1 --------------------------------
v = []
fl = []
l = []

def getln(st):
    for i in range(len(v)):
      if v[i] == st:
        return i

for i in range(len(f)):
    vi = f[i].split()
    v.append(vi[1])
    fl.append(int(vi[4][5:-1]))
    l.append([x.replace(',','') for x in vi[9:]])

lk = []    
for i in l:
    ls = []
    for j in i:
      ls.append(getln(j))
    lk.append(ls)

def getn():
  nds = []
  for i in range(len(fl)):
    if fl[i] > 0:
      nds.append(i)
  return nds

sp = 0
for i in range(len(v)):
    if v[i] == 'AA':
        sp = i
ns = [sp] + getn()

def getds(st,en):  # Find distance between valves st and en
  q = [(st,0)]    
  done = False
  been = []
  while not done:
    nd,ds = q[0]
    q = q[1:]    
    if nd == en:  
        done = True
        return ds
    if nd in been: continue
    been.append(nd)
    for d in lk[nd]: q.append((d,ds+1))

dss = []
for i in range(len(ns)):  
  dt = []
  for j in range(len(ns)): 
    dt.append(getds(ns[i],ns[j]))    
  dss.append(dt)

vo = []
bn = []
bst = [0]
bstpath = ['']
bstpathl = []

def sch(c,vo,tfl,m,pth,pthl,sc):
  ni = -1
  if len(sc) != 0: 
    ni = sc[0]
  for nn in range(len(ns)):
   if (ni == -1) or (v[ns[nn]] == ni):
    if dss[nn][c] <= m:
     if nn != sp:
      if nn != c:  
       if nn not in vo:    
        nvo = vo[:] + [nn]      
        ds = dss[c][nn] + 1
        if ds < m:
            npthl = pthl[:]
            npthl.append(v[ns[nn]])
            sch(nn,nvo,tfl+ds*sum([fl[ns[x]] for x in vo]),m-ds,pth+' to '+v[ns[nn]],npthl,sc[1:])                
  
  rest = tfl+m*sum([fl[ns[x]] for x in vo])
  bst.append(rest)  
  bstpath.append(pth)
  bstpathl.append(pthl[:])


tfl = 0
m = 30
sch(0,[],tfl,m,'AA',['AA'],[])
bpath = ''

print('part 1 -',max(bst))

# Part 2 ---------------------------------------------------

vo = []
bn = []
bst = []
bstpath = ['']
bstpathl = []   # Set of all possible paths

tfl = 0
m = 26

sch(0,[],tfl,m,'AA',['AA'],[])

bstn = 0
bpth = []

sl = []
setl = []
fs = set()  # Full set - all paths found
for i in range(len(bstpathl)):
    fs.add(i)   

bcw = {}
for i in range(len(ns)): # for each working valve in the puzzle
    bcw[v[ns[i]]] = i
    nf = []
    stl = set()  
    for j in range(len(bstpathl)):       
      if v[ns[i]] not in bstpathl[j]:  # work out which paths did not visit the valve
        nf.append(j)  
        stl.add(j)
    sl.append(nf)
    setl.append(stl)

for i in range(len(bstpathl)):  # Go through each path possible
   if i%1000==0:
    print('progress',i,'of',len(bstpathl) )       
   cd = set()    
   cd = cd.union(fs) # Get a full set of paths
   for el in bstpathl[i][1:]:  # go through each element of the current path being considered       
    cd = cd.intersection(sl[bcw[el]])   # set intersection to narrow down mutually exclusive path numbers,     
                                        # eliminating the paths that have visited 'el' (i.e. an element of current path being considered)
   for k in cd:  # Get a list of mutually exclusive paths ('cd')    
    if bst[i] + bst[k] > bstn:  # If best so far
        bstn = bst[i] + bst[k]            
        bpth = [bstpathl[i],bstpathl[k]]
        print('part 2 - best so far',bstn,'path',bpth,bst[i],bst[k])


# Dave's solution, pt1 - 1741, pt2 - 2316
# Ken Solution, pt1 - 1906, pt2 - 2548
# Example Solution pt1 - 1651, pt2 - 1707
