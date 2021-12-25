f = open('21-25.txt').read().split('\n')
c = []
for i in f:
    r = []
    for hr in i: r.append(hr)
    c.append(r)
szx,szy = len(c),len(c[0])
dn = False
k = 1
while not dn:
 dn = True                    
 for d in [0,1]:
  nc = [e[:] for e in c]  
  for i in range(szx):
    for j in range(szy):        
        if d == 0 and c[i][j] == '>':            
            if c[i][(j+1)%szy] == '.':
                nc[i][j] = '.'                
                nc[i][(j+1)%szy] = '>'
                dn = False                
        if d == 1 and c[i][j] == 'v':          
            if c[(i+1)%szx][j] == '.':
                nc[i][j] = '.'
                nc[(i+1)%szx][j] = 'v'
                dn = False  
  c = [e[:] for e in nc]
 print('step',k)
 k += 1
print('part 1',k-1)
