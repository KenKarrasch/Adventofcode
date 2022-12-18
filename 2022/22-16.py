f = open('22-16.txt').read().split('\n')

# Part 1 - 
#  Start by getting the distances between valves this non zero flow rates, use BFS.
#  Then recursively search these nodes to find the best route.

# Part 2 - 
#  set timer to 26 mins.
#  do a search as before, taking note to the path taken
#
#  go back and edit the input data, changes the flow rates to zero for all nodes visited by the first elephant.
#
#  Do the search again for the second elephant, (he wont visit the same places as the first elephant
#  because we set the flow rates to zero)
#  
#  add the two 
#  
#  a few secs for both parts, alot quicker than I was expecting, internet has solution taking all night 
#  for alot of people, not sure how they are doing it.
#

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


def sch(c,vo,tfl,m,pth,sc):
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
            sch(nn,nvo,tfl+ds*sum([fl[ns[x]] for x in vo]),m-ds,pth+' to '+v[ns[nn]],sc[1:])        
         
  if True:
        rest = tfl+m*sum([fl[ns[x]] for x in vo])
        bst.append(rest)  
        bstpath.append(pth)

 
tfl = 0
m = 30
sch(0,[],tfl,m,'AA',[])
bpath = ''

print('part 1 -',max(bst))

# Part 2 ---------------------------------------------------


vo = []
bn = []
bst = [0]
bstpath = ['']

tfl = 0
m = 26

sch(0,[],tfl,m,'AA',[])
bpath = ''

p2 = max(bst)
print('1st elephant releases pressure',p2)

for i in range(len(bst)):
  if bst[i] == max(bst):
    bpath = bstpath[i].split(' to ')
    break

v = []
fl = []
l = []

for i in range(len(f)):
    vi = f[i].split()
    v.append(vi[1])    
    if vi[1] not in bpath:
       fl.append(int(vi[4][5:-1]))
    else:
        fl.append(0)
    l.append([x.replace(',','') for x in vi[9:]])

lk = []    
for i in l:
    ls = []
    for j in i:
      ls.append(getln(j))
    lk.append(ls)

ns = [sp] + getn()

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
 
tfl = 0
m = 26

sch(0,[],tfl,m,'AA',[])
bpath = ''
p2 += max(bst)
print('part 2 -',p2)
