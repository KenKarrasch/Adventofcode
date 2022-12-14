f = open('22-14.txt').read().split('\n')

# fun one after christmas party

mx = my = 0

for i in f:
  h = i.split('->')
  for k in h:
    j = [int(x.strip()) for x in k.split(',')]
    if mx < j[0]:
      mx = j[0]
    if my < j[1]:
      my = j[1]
        
g =[]
for i in range(my+2):
  l = []
  for j in range(mx+2):
      l.append('_')
  g.append(l)
    

for i in f:
  h = i.split('->')
  for j in range(len(h)-1):
    u = [int(x.strip()) for x in h[j].split(',')]
    v = [int(x.strip()) for x in h[j+1].split(',')]
    if u[1] == v[1]:
      st = min(u[0],v[0])
      ed = max(u[0],v[0])
      for d in range(ed+1-st):
        g[u[1]][st+d] = '#'
    else:
      st = min(u[1],v[1])
      ed = max(u[1],v[1])
      for d in range(ed+1-st):
        g[st+d][u[0]] = '#'
    
dn = False
sc = 500
c = 0

while not dn:
  c += 1
  rst = False
  sd = [500,0]
  while not rst:
    if sd[1] > len(g)-2:
      dn = True
      print 'part 1 -',c-1
      break
    if g[sd[1]+1][sd[0]] == '_':
      sd[1] += 1
    elif g[sd[1]+1][sd[0]-1] == '_':
      sd[0] -= 1
      sd[1] += 1
    elif g[sd[1]+1][sd[0]+1] == '_':
      sd[0] += 1
      sd[1] += 1
    else:
      rst = True
      g[sd[1]][sd[0]] = 'o'
      

mx = 1000

g =[]
for i in range(my+3):
  l = []
  for j in range(mx+2):
      l.append('_')
  g.append(l)


p1 = '0,'
p2 = str(my+2)
p3 = ' -> 999,'

f.append(p1+p2+p3+p2)

for i in f:
  h = i.split('->')
  for j in range(len(h)-1):
    u = [int(x.strip()) for x in h[j].split(',')]
    v = [int(x.strip()) for x in h[j+1].split(',')]
    if u[1] == v[1]:
      st = min(u[0],v[0])
      ed = max(u[0],v[0])
      for d in range(ed+1-st):
        g[u[1]][st+d] = '#'
    else:
      st = min(u[1],v[1])
      ed = max(u[1],v[1])
      for d in range(ed+1-st):
        g[st+d][u[0]] = '#'
    
dn = False

sc = 500
c = 0

while not dn:
  c += 1
  rst = False
  sd = [500,0]
  if g[sd[1]][sd[0]] == 'o':
    print 'part 2 -',c-1
    dn = True
  while not rst:
    if sd[1] > len(g)-2:
      dn = True
      print 'part 1 -',c-1
      break
    if g[sd[1]+1][sd[0]] == '_':
      sd[1] += 1
    elif g[sd[1]+1][sd[0]-1] == '_':
      sd[0] -= 1
      sd[1] += 1
    elif g[sd[1]+1][sd[0]+1] == '_':
      sd[0] += 1
      sd[1] += 1
    else:
      rst = True
      g[sd[1]][sd[0]] = 'o'
