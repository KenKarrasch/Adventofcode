from collections import deque

f = open('23-23.txt').read().split('\n')

gd = []
for r in range(len(f)):
    ln = []
    for c in range(len(f[r])):
        ln.append(f[r][c])
    gd.append(ln)

rs, cs = len(gd), len(gd[0])    
drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]    

def sch(s,e):    
    v = set()    
    Q = deque([(s[0],s[1],1,v,0)])  # (row, col, path_length)            
    while Q:        
      r, c, pl, v, ars = Q.popleft()                
      if (r,c) in v or r < 0 or c < 0 or r >= rs or c >= cs or gd[r][c] == '#':
        continue                      
      v.add((r, c))        
      if r == e[0] and c == e[1]:                
        return pl
      
      for dr, dc in drs:
        nr,nc = r+dr,c+dc
        ok = True        
        nars = ars
        if 0 <= nr < rs and 0 <= nc < cs:
         if gd[nr][nc] == '>':
           if (dr,dc) != (0,1):
            ok = False            
         if gd[nr][nc] == '<':
           if (dr,dc) != (0,-1):
            ok = False            
         if gd[nr][nc] == 'v':
           if (dr,dc) != (1,0):
            ok = False            
         if gd[nr][nc] == '^':
           if (dr,dc) != (-1,0):
            ok = False
         if gd[nr][nc] in '<>^v':           
           nars = ars + 1
        if ok:
         if (nr, nc) not in v:
          if nars < 3:
           Q.append((nr,nc,pl+1,v,nars))

for r in range(len(gd)):
   l = ''
   for c in range(len(gd[0])):
      l += gd[r][c]
   print(l,r)

nde = []

nde.append([0,1])
nde.append([rs-1,cs-2])

for r in range(rs):    
  for c in range(cs):
   if gd[r][c] == '.':  
    ct = 0    
    for dr, dc in drs:             
      nr,nc = r+dr,c+dc      
      if 0 <= nr < rs and 0 <= nc < cs:            
         if gd[nr][nc] in '<>v^':           
           ct += 1    
    if ct > 1:      
      nde.append([r,c]) 


dss = []

for s in nde:
  for e in nde:
   if s != e:
    d = sch(s,e)    
    if d != None:
      dss.append([s,e,d])
       
for i in dss:
  print(i)

print('-----------------')

pths = []

def schn(s,e):
    v = set()    
    bn = []
    Q = deque([(s[0],s[1],1,bn)])  # (row, col, path_length)  
    print(Q)          
    while Q:   
      print(Q)     
      r, c, pl, nbn = Q.popleft()    
      if [r,c] in nbn:
        continue
      nbn.append([r, c])  
      if [r,c] == e:
        pths.append(pl)
        continue
      for i in dss:
        if i[0] == [r,c]:          
          nnbn = nbn[:]          
          Q.append((dss[1][0],dss[1][1],pl+i[2],nnbn))

ds = []

def schnr(s,e,d,bn):
    global ds
    for i in dss:      
      if i[0] == s:
       if i[1] == e:
        #print(i[1],e,[d+i[2],bn])
        ds.append([d+i[2]-len(bn)-1,bn])                    
       if i[1] not in bn:
        nbn = bn[:]
        nbn.append(i[1][:])
        schnr(i[1],e,d+i[2],nbn)
    
schnr([0,1],[rs-1,cs-2],0,[])

print('dests')
bst = 0
for i in ds:
    if i[0] > bst:
      bst = i[0]
    print(i)
print('part 1',bst)
