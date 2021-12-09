f = [ i for i in open('21-9.txt').read().split('\n')]

g = []
isl = []
ct = [0]
mx = []
for i in f:
    h = []
    bn = []
    for c in i:
        h.append(int(c))
        if int(c) != 9:
            bn.append('.')
        else: bn.append('X')
    g.append(h)
    isl.append(bn)
sy = len(f)
sx = len(f[0])

ss = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

ssd = [[-1,0],[0,-1],[0,1],[1,0]]


def gv(x,y):
    if x < 0 or y < 0:
       return 10
    if x > sx-1 or y > sy-1:
      return 10
    return g[y][x]

def expl(x,y,dp):
  isl[y][x] = 'z'
  for xd in ssd:
    dy = y+xd[1]
    dx = x+xd[0]
    if gv(dx,dy) != 10:
      if isl[dy][dx] == '.':
        isl[dy][dx] = 'X'
        ct[0] += 1
        expl(dx,dy,dp+1)

def adj(x,y):
    v = g[y][x]
    a = 0
    gd = True
    for xd in ss:
        s = gv(x+xd[0],y+xd[1])
        if v > s:
            gd = False
            a += s
    if gd: return v + 1
    else: return 0

t = 0
for y in range(sy):
    for x in range(sx):
        t += adj(x,y)
print 'part 1 -',t

tl = 1
for ys in range(sy):
    for xs in range(sx):
        ct[0] = 1
        if isl[ys][xs] == '.':
            expl(xs,ys,0)
            mx.append(ct[0])
mx.sort()
k = len(mx)
print 'part 2 -',mx[k-1]*mx[k-2]*mx[k-3]
