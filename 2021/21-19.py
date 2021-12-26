import copy
from typing import AbstractSet

# Warning - this is not a general solution, it will only work on my solution.  Human intervention has been made to join groups of scanners 
# 
# 48 different orientations, = 8 x 6, 8 pos/negs for 2 dimensions,  6 ways of rotating, (6 faces on a cube)
# To match scanners I began by calculating the pythagorus dist between each combination of datapoints for each scanner
# If a scanner has say 25 datapoints there will be 25x25 = 625 pairs
#
# Then I compared each pair of scanners to see if they had some signatures in common, I made a list of scanner pairs.
# Note: there were some collisions, so make sure there are in fact 12 pairs. 
#
# Then computed a graph show linking the scanners.
#
# I then walked through the graph, firstly confirming the actual datapoints, and then rightsiding all the scanner points.
#
# Unfortunately the problem implies that this strategy would work, which is possibly misleading.
#
# "The scanners and beacons map a single contiguous 3d region. This region can be reconstructed by finding pairs of scanners
#  that have overlapping detection regions such that there are at least 12 beacons
#  that both scanners detect within the overlap"
#
# This was not the case for my data.  When constructing the graph 3 contiguous areas formed, not one.
#
# I had to manual combine pairs with other pairs to join the regions. 
#
#  Debug comments left in.
#


f = open('21-19.txt').read().split('\n\n')

rots = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

polsz = [[1,1,1],[-1,-1,1],[-1,1,1],[1,-1,1],[-1,-1,-1],[-1,1,-1],[1,-1,-1],[1,1,-1]]

sc = []
for i in f:    
    scn = []
    for j in i.split('\n')[1:]:
        c = [int(k) for k in j.split(',')]
        scn.append(c)
    sc.append(scn)

scs = []

def trfm(bs,r,p):
    nbs = []        
    for i in bs:        
        ns = []
        for d in [0,1,2]: # 3 dimensions                
            ns.append(i[rots[r][d]])
        for d in [0,1,2]:
            ns[d] *= polsz[p][d]
        nbs.append(ns)
    return nbs

p = []
tm = []
for i in range(len(sc)):
    tm.append([-1,-1])

for i in range(len(sc)):
    p.append([-1,-1,-1])

p[0] = [0,0,0]
tm[0] = [0,0]

dl = [0]
ex = []
done = False
s1 = [i[:] for i in sc[0]]
os1 = [i[:] for i in s1]
s = 1

sgn = [] 

def getsgns(gsc):
 # Get layout signatures
 sgnn = []
 ls = []
 for i in gsc:
  sg = []
  sr = range(len(i))
  for g in sr:
    for h in sr:
       if g != h:
         pyt = 0
         for d in [0,1,2]:
            ds = i[g][d] - i[h][d]
            pyt += ds*ds
         sg.append(pyt)
  sgnn.append(sg)
  ls.append(len(sg))
 return sgnn
  
def getcms(sgn,scs):
 # find pairs
 cms = []
 cpt = []
 for i in range(len(scs)):
  dn = False
  cpti = []
  for j in range(len(scs)):
   if not dn:
    cm = 0
    if i != j:
      for k in sgn[i]:
        for l in sgn[j]:
          if k == l:
            cm += 1
            cpti.append(sgn[i][1])
            #if i == 35 and j == 0:
            #    print( k,l,cm)
    if cm > 10:
      if [i,j] not in cms:
        if [j,i] not in cms:
          #if i == 0 and j == 35:
          #    print( i,j,cm)
          #if j == 0 and i == 35:
          #    print( j,i,cm)
          cms.append([i,j])
      dn = True
   cpt.append(cpti)
 return cms
      

def getgp(num,cms):
  # get scanners that can be paired
  gp = [num]
  while len(gp) < len(sc):   
   sz = len(gp)
   for i in cms:
      for j in gp:
          if i[0] == j:
             if i[1] not in gp:
                 gp.append(i[1])
          if i[1] == j:
             if i[0] not in gp:
                 gp.append(i[0])
   if len(gp) == sz:       
       return gp

def getlsts(cms,gc):
  #get a list of contiguous groups
  #of scanners
  lsts = []
  for i in range(len(gc)):
    nl = getgp(i,cms)
    nl.sort()
    if nl not in lsts:
        lsts.append(nl)
  return lsts
  
def getn(st):
  for i in cms:
    if st in i:
      if i[0] == st:
        if i[1] not in dl:
            return i[1],st
      else:
        if i[0] not in dl:
            return i[0],st
            
def gettree(st,bn,cmsn):
  nl = bn[:]
  for i in cmsn:
    if st in i:
      if i[0] == st:
        if i[1] not in bn:
            nl.append(st)
            schp.append([st,i[1]])
            gettree(i[1],nl,cmsn)
      if i[1] == st:
        if i[0] not in bn:
            nl.append(st)
            schp.append([st,i[0]])
            gettree(i[0],nl,cmsn)
            
ab = []

def getgd(s,nn,gb,p,tm,comb):
    s1 = [i[:] for i in gb[s]]
    print(s)
    print(nn)
    s2 = [i[:] for i in gb[nn]]  
    dn = False
    for j in s2:
      print((j))
      for i in s1:
       if not dn:
        for r in range(len(rots)):  
         for px in [-1,1]:
          for py in [-1,1]:   
           for pz in [-1,1]:                      
             x = i[0]-j[rots[r][0]]*px
             y = i[1]-j[rots[r][1]]*py
             z = i[2]-j[rots[r][2]]*pz
             for k in range(6):  
               for l in range(8):                            
                 ns2 = trfm(s2,k,l)                            
                 ct = 0                                   
                 for b in s1:                          
                    nb = [b[0]- \
                     x,b[1]-y,b[2]-z]                        
                    if nb in ns2:                           
                      ct += 1                             
                 if ct > 2:
                     print((rots[k],\
                        polsz[l],ct,\
                        x,y,z))
                     dn = True
                     tm[nn] = [k,l]
                     p[nn] = [x,y,z]

    s2 = trfm(s2,tm[nn][0],0)
    s2 = trfm(s2,0,tm[nn][1])
    ns2 = []    
    for i in s2:
        ns2.append([i[0]+p[nn][0],\
                i[1]+p[nn][1],\
                i[2]+p[nn][2]])
    if comb:
      for i in ns2:
        if i not in s1:
          s1.append(i[:])
      gb[s] = [i[:] for i in s1]
      gb[nn] = []
    else:
       gb[nn] = [i[:] for i in ns2]
    
    print('p',p)
    print('tm',tm)
    for i in s1:
      if i not in ab:
        ab.append(i[:])
    s = nn
    return gb,p,tm

if True:
 sgn = getsgns(sc)
 cms = getcms(sgn,sc)
 lsts = getlsts(cms,sc)

 print(('-----'))
 print( 'contiguous')
 for i in lsts:
    print( (i))
 schp = []
 gettree(0,[],cms)
 print( 'schp',schp)

 ab = []
 dl = [0]

if True:
 #print( sc)
 ndb = copy.deepcopy(sc)
 np = copy.deepcopy(p)
 ntm = copy.deepcopy(tm)

 for i in [[0,5]]: # Helping hand to join contiguous groups of scanners
    print( i)
    hg,hp,htm = getgd(i[0],i[1],ndb,p,tm,True)
    ndb = copy.deepcopy(hg)
    np = copy.deepcopy(hp)
    ntm = copy.deepcopy(htm)
    dl.append(i[1])
    
 sgn = getsgns(ndb)
 cms = getcms(sgn,ndb)
 lsts = getlsts(cms,ndb)
 
 print( cms)
 print(('-----'))
 print( 'contiguous')
 for i in lsts:
    print( (i))
 schp = []
 gettree(0,[],cms)
 print( 'schp',schp)

if True:
 ndb = copy.deepcopy(ndb)
 np = copy.deepcopy(p)
 ntm = copy.deepcopy(tm)
 
 for i in [[0,1]]:  # Helping hand to join contiguous groups of scanners
    hg,hp,htm = getgd(i[0],i[1],\
       ndb,p,tm,True)
    ndb = copy.deepcopy(hg)
    np = copy.deepcopy(hp)
    ntm = copy.deepcopy(htm)
    dl.append(i[1])
    
 sgn = getsgns(ndb)
 cms = getcms(sgn,ndb)
 lsts = getlsts(cms,ndb)

 print( cms)
 print(('-----'))
 print( 'contiguous')
 for i in lsts:
    print( (i))
 schp = []
 gettree(0,[],cms)
 print( 'schp',schp)
 print( 'dl',dl)
 
if True:
 ndb = copy.deepcopy(ndb)
 np = copy.deepcopy(p)
 ntm = copy.deepcopy(tm)
 
 for i in [[0,13]]: # Helping hand to join contiguous groups of scanners
    hg,hp,htm = getgd(i[0],i[1],\
       ndb,p,tm,True)
    ndb = copy.deepcopy(hg)
    np = copy.deepcopy(hp)
    ntm = copy.deepcopy(htm)
    dl.append(i[1])
    
 sgn = getsgns(ndb)
 cms = getcms(sgn,ndb)
 lsts = getlsts(cms,ndb)

 print( cms)
 print(('-----'))
 print( 'contiguous')
 for i in lsts:
    print( (i))
 schp = []
 gettree(0,[],cms)
 print( 'schp',schp)
 print( 'dl',dl)

if True:
 ndb = copy.deepcopy(ndb)
 np = copy.deepcopy(p)
 ntm = copy.deepcopy(tm)
 
 for i in [[0,2]]:  # Helping hand to join contiguous groups of scanners
    hg,hp,htm = getgd(i[0],i[1],\
       ndb,p,tm,True)
    ndb = copy.deepcopy(hg)
    np = copy.deepcopy(hp)
    ntm = copy.deepcopy(htm)
    dl.append(i[1])
    
 sgn = getsgns(ndb)
 cms = getcms(sgn,ndb)
 lsts = getlsts(cms,ndb)

 print( cms)
 print(('-----'))
 print( 'contiguous')
 for i in lsts:
    print( (i))
 schp = []
 gettree(0,[],cms)
 print( 'schp',schp)
 print( 'dl',dl)
 
 
if True:
 ndb = copy.deepcopy(ndb)
 np = copy.deepcopy(p)
 ntm = copy.deepcopy(tm)
 
 for i in [[0,35]]: # Helping hand to join contiguous groups of scanners
    hg,hp,htm = getgd(i[0],i[1],\
       ndb,p,tm,True)
    ndb = copy.deepcopy(hg)
    np = copy.deepcopy(hp)
    ntm = copy.deepcopy(htm)
    dl.append(i[1])
    
 sgn = getsgns(ndb)
 cms = getcms(sgn,ndb)
 lsts = getlsts(cms,ndb)

 print( cms)
 print(('-----'))
 print( 'contiguous')
 for i in lsts:
    print( (i))
 schp = []
 gettree(0,[],cms)
 print('schp',schp)

if True:  # Now we have one large group of contiguous scanners, work throught the rest
 for i in schp:
    hg,hp,htm = getgd(i[0],i[1],\
     ndb,p,tm,False)
    ndb = copy.deepcopy(hg)
    np = copy.deepcopy(hp)
    ntm = copy.deepcopy(htm)
    dl.append(i[1])
    
    sgn = getsgns(ndb)
    cms = getcms(sgn,ndb)
    lsts = getlsts(cms,ndb)

    print( cms)
    print(('-----'))
    print( 'contiguous')
    for i in lsts:
       print( (i))
    schp = []
    gettree(0,[],cms)
    print( 'schp',schp)
    print( 'done list', dl)
    print( 'ab',ab,len(ab))

#p = [[0, 0, 0], [37, -80, -2444], [1245, 2227, -4750], [1209, 1115, -2505], [3577, 2304, -3694], [1130, 1142, -1272], [0, -31, 1119], [1216, 3439, -4790], \
    # [-86, 1149, -2358], [-1321, 2, -46], [2404, 2318, -3662], [1160, 1099, -6084], [27, 3540, -2514], [-31, 1180, -3732], [-1186, 1025, -3561], [1184, 2246, -1175],     
    # [3660, 3611, -3682], [3541, 2416, -1333], [-49, -24, -1280], [2385, 2256, -1269], [-1314, 2341, -1255], [1173, 1062, -4865], [-1255, 1192, -127], [1261, -21, -2424], \
    # [-1162, 1081, -1316], [69, 2375, -7236], [-126, 2258, -2504], [1121, 2312, -3580], [-2357, 1058, -1236], [1254, 2329, 40], [40, 2228, -1279], [1238, -178, -78], \
    # [1211, 2274, -5952], [3615, 2401, -4791], [-1178, 2303, -2387], [-125, 2374, -5970], [65, 1168, -1208], [1165, 2344, -2394], [1116, 3482, -5996]]

#tm = [[0, 0], [1, 2], [2, 2], [0, 6], [1, 7], [0, 5], [4, 5], [1, 4], [4, 6], [5, 3], [5, 7], [2, 4], [3, 6], [2, 3], [3, 1], [1, 3], [5, 2], [5, 4], [0, 1], [3, 5], \
#      [4, 1], [4, 0], [2, 7], [3, 0], [3, 6], [1, 7], [5, 3], [5, 4], [4, 1], [5, 7], [4, 6], [3, 5], [5, 2], [4, 0], [3, 5], [0, 1], [5, 7], [0, 6], [0, 5]]

ab = []
gb = copy.deepcopy(sc)
print('amalgamating')
for nn in range(1,len(gb)):
    s = 0    
    s2 = [i[:] for i in gb[nn]] 
    s1 = [i[:] for i in gb[s]] 
    print('s1',s1)
    print
    print('s2',s2)
    print
    s2 = trfm(s2,tm[nn][0],0)
    s2 = trfm(s2,0,tm[nn][1])
    ns2 = []    
    for i in s2:
        ns2.append([i[0]+p[nn][0],\
                i[1]+p[nn][1],\
                i[2]+p[nn][2]])
    gb[nn] = [i[:] for i in ns2]    
    if True:
      for i in ns2:
        if i not in s1:
          s1.append(i[:])
      gb[s] = [i[:] for i in s1]
      gb[nn] = []
    for i in s1:
      if i not in ab:
        ab.append(i[:])
    s = nn    
    print('ab',ab)

print('part 1 -',len(ab))

md = []
for i in p:
  for j in p:
    ds = 0
    for d in [0,1,2]:
      ds += abs(i[d]-j[d])
    md.append(ds)      

print('part 2 -',max(md))
