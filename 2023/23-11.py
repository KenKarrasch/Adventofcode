f = open('23-11.txt').read().split('\n')

for gap in [1,999999]: 
 r,c,prs,ep = [],[],[],[]
 for i in range(len(f)):        
    l = 0
    for j in range(len(f[0])):        
        if f[i][j] == '#':
            prs.append([i,j])
            l += 1     
    if l == 0: r.append(i)  
 
 for i in range(len(f[0])):        
    l = 0
    for j in range(len(f)):
        if f[j][i] == '#': l += 1 
    if l == 0:
        c.append(i)  
 
 for i in prs:
    x,y = i    
    for rw in r:
        if i[0] > rw: x += gap
    for cl in c:        
        if i[1] > cl: y += gap  
    ep.append([x,y])
 
 d = 0
 for p1 in range(len(ep)):
  for p2 in range(p1+1,len(ep)):  
   if p1 != p2:
    r1,r2 = ep[p1],ep[p2]    
    d += abs(r1[0]-r2[0]) + abs(r1[1]-r2[1])        
 
 if gap == 1: print('part 1',d)
 else: print('part 2',d)
