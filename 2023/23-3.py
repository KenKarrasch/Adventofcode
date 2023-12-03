r = open('23-3.txt').read().split('\n')

num = '1234567890'

ss = [[-1,-1],[-1,0],[-1,1],  [0,-1],[0,1], [1,-1],[1,0],[1,1]]
ssw = [[0,-1],[0,1]]

def schsw(sh,gr):
  fd = False
  if 0 <= sh[0] < len(r):    
    if 0 <= sh[1] < len(r[0]):    
        if gd[sh[0]][sh[1]]:
            return
        if r[sh[0]][sh[1]] == '.':
            return
        if r[sh[0]][sh[1]] in num:
           gd[sh[0]][sh[1]] = 1
           if gr != -1:
               gsd[sh[0]][sh[1]] = gr+1
           fd = True
        for sp in ssw:
            schsw([sp[0] + sh[0], sp[1] + sh[1]],gr)
  return fd

def sch(sh,gr):
  gs = 0
  if 0 <= sh[0] < len(r):    
    if 0 <= sh[1] < len(r[0]):    
        if gd[sh[0]][sh[1]]:
            return
        if r[sh[0]][sh[1]] == '.':
            return
        if r[sh[0]][sh[1]] in num:
           gd[sh[0]][sh[1]] = 1
           if gr != -1:
             gsd[sh[0]][sh[1]] = gr+1
        for sp in ss:
          if schsw([sp[0] + sh[0], sp[1] + sh[1]],gr):
               gs += 1
  if gs == 2:
      return True
  else: return False

sm = []
g = []

for i in range(len(r)):
  for j in range(len(r[0])):
    if r[i][j] not in num:
      if r[i][j] != '.':
        sm.append([i,j])
    if r[i][j] == '*':
       g.append([i,j])

gd = []
gsd = []

for i in range(len(r)):
  l = []
  for j in range(len(r[0])):
    l.append(0)
  lg = l[:]
  gd.append(l)
  gsd.append(lg)

for i in sm:
  gr = -1
  if i in g:
     for j in range(len(g)):
        if g[j] == i:
            gr = j
  sch(i,gr)

ty,fa,nums = 0, [], []

for i in g:
  fa.append([0,0])
  
for i in range(len(gd)):
   nw = ''
   gear = 0
   for j in range(len(gd[i])):      
      if gd[i][j] == 1:
         nw += r[i][j]        
         gear = gsd[i][j]
      else:
         if nw != '':         
            if gear != 0:
             if fa[gear-1][0] == 0:
              fa[gear-1][0] = int(nw)
             else:
              fa[gear-1][1] = int(nw)
            ty += int(nw)
            nw = ''
   if nw != '':
       if gear != 0:
        if fa[gear-1][0] == 0:
          fa[gear-1][0] = int(nw)
        else:
          fa[gear-1][1] = int(nw)
       ty += int(nw)

print 'part 1',ty
pt2 = 0
for i in fa:
    pt2 += i[0]*i[1]

print 'part 2',pt2
