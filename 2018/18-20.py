p = open('18-20.txt').read().split('\n')
sz = 100
g = [['.' for x in range(sz)] for y in range(sz)]
gd = [[0 for x in range(sz)] for y in range(sz)]
move = [[0,1,-1,0],[-1,0,0,1]]

def fb(i, p):
    depth = 0
    for h in range(i,len(p)):
      if p[h] == '(':
        depth += 1
      if p[h] == ')':
        depth -= 1
        if depth == 0:
          return h
    return -1

def walk(x,y,p,gr,d):
  st = [x,y]
  sd,i = d,0
  while i < len(p):
    if p[i] != '(' and p[i] != '|':
      d += 1
      x += move[0]['NEWS'.index(p[i])]
      y += move[1]['NEWS'.index(p[i])]
      if g[x][y] != 'X':
        gd[x][y] = d
      g[x][y] = 'X'
    if p[i] == '(':
      e = fb(i,p)
      walk(x,y,p[i+1:e],gr,d)     
      i = e
    if p[i] == '|':
      x,y,d = st[0],st[1],sd
    i += 1

walk(sz/2,sz/2,p[0][1:-1],g,0)
maxd,sh = 0,0
for l in gd:
  if maxd < max(l):
    maxd = max(l)  
  for g in l:
    if g >= 1000:
      sh += 1
print 'part 1 -',maxd
print 'part 2 -',sh
