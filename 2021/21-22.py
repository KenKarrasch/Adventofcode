import copy

f = open('21-22.txt').read().split('\n')

al = []
ss = []

for i in f:
    dt = i.split()
    al.append(dt[0])
    cb = []
    for d in [0,1,2]:
      cb.append([int(j) for j in dt[1].split(',')[d].split('=')[1].split('..')])
    ss.append(cb)

ncb = []
      
def overlaps(a,bi):
 # work out if a overlaps b
 b = bi[0]
 for d in [0,1,2]:
    if a[d][1] < b[d][0] or \
       a[d][0] > b[d][1]:
        return False
 return True
 
 
def tidyup(ci):
 # this code never worked but 
 # would in theory speed up processing
 # by amalgamating cubes next to
 # each other
 dn = False
 c = copy.deepcopy(ci)
 while not dn:
  no = []
  ld = False
  dn = True
  for hi in range(len(c)):
   for ji in range(len(c)):
    if not ld:
     h = c[hi][0]
     j = c[ji][0]
     if c[hi][1] == c[ji][1]:
      ds = []
      for d in [0,1,2]:
        if h[d] == j[d]:
          ds.append(d)
      if len(ds) == 2:
        for d in [0,1,2]:
          if d not in ds:
            cl = []
            for hy in [0,1]:
              cl.append(h[d][hy])
              cl.append(j[d][hy])
            cl.sort()
            if cl[1] == cl[2]-1:
              nb = [0,0,0]
              nb[d] = [cl[0],cl[-1]]
              dn = False
              for e in [0,1,2]:
                if d != e:
                  nb[e] = h[e][:]
              no = [hi,ji,\
                  nb,c[hi][1]]
              print 'no',no
              ld = True
  if len(no) > 0:
    lg = [no[0],no[1]]
    lg.sort()
    del c[lg[1]]
    del c[lg[0]]
    c.append([no[2],no[3]])
 return c
             
def countcb(c):
  # get size of cubes
  tl = 0
  for i in c:
    b = i[0]
    if i[1] == 'on':
      m = 1
      for d in [0,1,2]:
        m *= 1+b[d][1]-b[d][0]
      tl += m
  return tl

  
def hb(i):
    # discard zero volume cubes
    for d in [0,1,2]:
        if i[d][0] > i[d][1]:
            return False
    return True

def spl(ai,bi):
  # split cube into pieces if there
  # is an overlap with another cube
  a = ai[0]
  b = bi[0]
  ap = ai[1]
  bp = bi[1]
  t = []
  for d in range(3):
    cp = []
    k = []
    for h in [0,1]:
       k.append(a[d][h])
       k.append(b[d][h])
    k.sort()
    u = [[k[0],k[1]-1],\
         [k[1],k[2]],\
         [k[2]+1,k[3]]]
    t.append(u)
  cb = []
  ca = []
  for x in [0,1,2]:
    for y in [0,1,2]:
      for z in [0,1,2]:
        i = [t[0][x],t[1][y],\
            t[2][z]]
        if hb(i):
          if overlaps(b,[i,'on']):
            cb.append([i,bp])
          if overlaps(a,[i,'on']):
            ca.append([i,ap])
  cm = []
  for i in ca:
    cm.append(i)
  for i in cb:
    if [i[0],bp] not in cm:
     if [i[0],ap] not in cm:
      cm.append(i)
  return cm
  #tm = tidyup(cm)
  # amalgamate blocks where possible
  #return tm
        
def addcb(nc,pl):
    # add cuboid
    # if the new cuboid overlaps with
    # another cube split both cubes
    # into smaller cubes.
    # put smaller cubes onto a stack
    # and see if they overlap with
    # any other cubes
    nb = []
    a = [[nc,pl]]
    print 'adding',a
    while len(a) > 0:
     cb = copy.deepcopy(a[0])
     i = 0
     hl = []
     dn = False
     while i < len(ncb) and not dn:
       if overlaps(cb[0],ncb[i]):
        nc = spl(cb,ncb[i])
        for j in nc:
         if not overlaps(j[0],ncb[i]):
            a.append(j)
         else:
           if j[1] == 'on':
             ncb.append(j)
        del ncb[i]
        dn = True
       i += 1
     if not dn:
        ncb.append(cb)
     del a[0]

pt1dn = False
ct = 1
for i in range(len(al)):
    if ss[i][0][0] > 51 or \
       ss[i][0][0] < -51:
      if not pt1dn:
        print 'part 1 -',ctr
        print
        pt1dn = True
    print ct, 'of', len(al)
    addcb(ss[i],al[i])
    ctr = countcb(ncb)
    print ctr
    print('========')
    ct += 1
print 'part 2 -',ctr
