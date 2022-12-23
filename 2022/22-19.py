from collections import defaultdict, deque

f = open('22-19.txt').read().split('\n')

# Made use of Deque data structure, it seems 
# to be 100 times faster than list structure

# key heuristics are:

# - dont build more robots than needed
# - discard resources that cannot ever be used (it helps with dp pruning)
# - discard unuasable resources towards the end of the 24 mins

o,c,ob,g = [],[],[],[]

for i in f:
    a = i.split()
    o.append(int(a[6]))
    c.append(int(a[12]))
    ob.append([int(a[18]),int(a[21])])
    g.append([int(a[27]),int(a[30])])
    
    
def getgeodes(bp,ms):
  qd = [(1,0,0,0,0,0,0,0,ms)]
  DP = set()
  # Maximum demand
  md = [0,0,0]
  md[0] = max(o[bp],c[bp], \
           ob[bp][0],g[bp][0])
  md[1] = ob[bp][1]
  md[2] = g[bp][1]
  bgeode = 0
  ct = 0
  while len(qd) > 0:
    (ro,rc,rob,rg,ao,ac, \
     aob,ag,m) = qd.pop()
    if ag > bgeode:
        bgeode = ag
        #print ao,ac,aob,ag
        #print ro,rc,rob,rg
        #print ag
    if m == 0:
       continue
       
    a = [ao,ac,aob,ag]
    r = [ro,rc,rob,rg]
    
    for j in [0,1,2]:
      if r[j] > md[j]:
        r[j] = md[j]
        
    # no point making more robots
    # if their product can't be consumed
    
    if a[0] > md[0]*m - r[0]*(m-1):
       a[0] = md[0]*m - r[0]*(m-1)
       
       
        #print 'ore reduced' because
        # no way of spending it in
        # the time left
    
    if a[1] > md[1]*m - \
              r[1]*(m-1):
       a[1] = md[1]*m - \
              r[1]*(m-1)
        
        #print 'clay reduced' because
        # no way of spending it in
        # the time left
    
    if a[2] >  md[2]*m - r[2]*(m-1):
        a[2] = md[2]*m - r[2]*(m-1)
    
    
    sg = (a[0],a[1], \
          a[2],a[3], \
          r[0],r[1], \
          r[2],r[3], \
              m)
      
    if sg in DP:
         #hits[0] += 1
         continue
    DP.add(sg)
      
    qd.append((r[0],r[1],r[2],r[3], \
           r[0]+a[0], \
           r[1]+a[1], \
           r[2]+a[2], \
           r[3]+a[3],m-1))
           
    if a[0] >= o[bp]:
       qd.append(
          (r[0]+1,r[1],r[2],r[3], \
           r[0]+a[0]-o[bp], \
           r[1]+a[1], \
           r[2]+a[2], \
           r[3]+a[3],m-1))
           
    if a[0] >= c[bp]:
       qd.append(
          (r[0],r[1]+1,r[2],r[3], \
           r[0]+a[0]-c[bp],
           r[1]+a[1], \
           r[2]+a[2], \
           r[3]+a[3],m-1))
           
    if (a[0] >= ob[bp][0]) \
       and (a[1] >= ob[bp][1]):
       qd.append(
          (r[0],r[1],r[2]+1,r[3], \
           r[0]+a[0]-ob[bp][0], \
           r[1]+a[1]-ob[bp][1], \
           r[2]+a[2], \
           r[3]+a[3],m-1))
           
    if (a[0] >= g[bp][0]) \
       and (a[2] >= g[bp][1]):
       qd.append( \
          (r[0],r[1],r[2],r[3]+1, \
           r[0]+a[0]-g[bp][0],
           r[1]+a[1], \
           r[2]+a[2]-g[bp][1], \
           r[3]+a[3],m-1))

  return bgeode
  
pt1 = 0
pt2 = 1
for b in range(len(o)):
    print 'blue print',b+1
    pt1 += (b+1)*getgeodes(b,24)
    
print 'part 1 -',pt1

for b in [0,1,2]:
    print 'blue print',b+1
    pt2 *= getgeodes(b,32)
        
print 'part 2 -',pt2
