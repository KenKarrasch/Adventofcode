from collections import deque
import random
import copy

# Used statistical approach, Ran a number of random searches between components,
# stored the pathways for each.
# Then look for hotspots where the paths go through the most.
# Eliminate the top 3, then see if splits the group

f = open('23-25.txt').read().split('\n')

wrs = []
itms = []
pths = {}
wrsd = {}

for i in f:    
    wre = i.split(':')
    if wre[0] not in itms:
     itms.append(wre[0])
    for i in wre[1].split():             
        wrs.append([wre[0],i])   
        wrs.append([i,wre[0]])   
        if i not in itms:
           itms.append(i)
for i in wrs:    
    wrsd[i[0]] = []

for w in wrs:    
  for i in itms: 
    if w[1] == i:
        wrsd[w[0]].append(i)

l = len(itms)

def linked(nwrs): 
 lst = []
 lst.append(nwrs[0][0])
 hp = True
 while hp:       
    hp = False       
    for i in nwrs:      
      if i[0] in lst:
        if i[1] not in lst:         
         lst.append(i[1])  
         hp = True        
      if i[1] in lst:  
        if i[0] not in lst:               
         lst.append(i[0])  
         hp = True    
    if len(lst) == l:
      return len(lst)
 return len(lst)

def fdpth(st,ed):    
    v = []    
    Q = deque([(st,v)])
    while Q:
      p,v = Q.popleft()          
      if p in v:
        continue      
      v.append(p)      
      if p == ed:        
        return v
      for i in wrsd[p]:         
        vn = v[:]
        Q.append((i,vn))

for i in wrs:
  pths[(i[0],i[1])] = 0

print('selecting random paths')

for i in range(50): # Increase this number to get better accuracy
  st = random.randint(0, len(itms)-1)
  ed = random.randint(0, len(itms)-1)
  if st != ed:    
    pth = fdpth(itms[st],itms[ed])
    print('pth',pth)
    for p in range(len(pth)-1):      
      sgn = [pth[p],pth[p+1]]
      sgn.sort()      
      sgnt = (sgn[0],sgn[1])
      if sgnt in list(pths.keys()):
        pths[sgnt] += 1

top = []
for i in list(pths.keys()):
  if pths[i] != 0:    
    top.append((pths[i],i))

top.sort()

print('most popular links')
tl = []
for i in top[::-1]:
    if len(tl) < 3:
      tl.append(i)
    print(i)
nwrs = copy.deepcopy(wrs)
poplist = []
for t in tl:   
  sgn = [t[1][0],t[1][1]]
  sgni = [t[1][1],t[1][0]]
  for i in range(len(nwrs)):
     if sgn == nwrs[i] or sgni == nwrs[i]:
       print(sgn)
       poplist.append(i)
poplist.sort()
print('Eliminate the top 3 links')
nwrs = copy.deepcopy(wrs)
for i in poplist[::-1]:
    poped = nwrs.pop(i)
print('Testing to see if it split the groups')
bl = linked(nwrs)
print('part 1',bl*(len(itms)-bl))
