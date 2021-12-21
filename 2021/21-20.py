inp = '21-20.txt'

f = open(inp).read().split('\n\n')

if 'test' in inp:
    s = ''
    for i in f[0].split('\n'):
        s += i    
else:
    s = f[0]
    
it = 50
d = f[1].split('\n')
szy = len(d)
szx = len(d[0])
gr = []
    
for i in range(szy+it*2+6):
    rw = []
    for j in range(szx+it*2+6):
        rw.append('.')
    gr.append(rw)
    
bl = [i[:] for i in gr]
    
for i in range(szy):
    for j in range(szx):
        gr[3+it+i][3+it+j] = d[i][j]

for lp in range(it):
  ngr = [i[:] for i in bl]
  if gr[1][1] == '.':
      cp = '#'
  else:
      cp = '.'
  if True:
    for u in range(szx+2*it+6):
      ngr[u][0] = cp
      ngr[0][u] = cp
      ngr[szy+it*2+6-1][u] = cp
      ngr[u][szy+it*2+6-1] = cp
  for u in range(1,szy+2*it+6-1):
    for v in range(1,szx+2*it+6-1):                          
       b = ''
       for x in [-1,0,1]:
        for y in [-1,0,1]:                
          if gr[u+x][v+y] == '#':        
                b = b + '1'
          else:
                b = b + '0'        
          idx = int(b,2)    
       if s[idx] == '#':                
         ngr[u][v] = '#'
  gr = [i[:] for i in ngr]
  print lp+1
  
  ct = 0
  for i in gr:
    for j in i:
        if j == '#':
            ct += 1

  if 1+lp == 2:
    print 'part 1 -',ct
print 'part 2 -',ct
