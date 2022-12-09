f = open('22-9.txt').read().split('\n')
# fun ropey puzzle

mv = []
for m in f:
    i = m.split()
    mv.append([i[0],int(i[1])])

d = {'R':[1,0],'L':[-1,0],'U':[0,-1],'D':[0,1]}

def md(a,b):
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    if abs(dx) == 2:
      if abs(dy) == 2:
        return(-dx/2,-dy/2)
    if dx > 1: return -1,-dy
    if dx < -1: return 1,-dy
    if dy > 1: return -dx,-1
    if dy < -1: return -dx,1
    return [0,0]

st = [0,0]
t = [st[::] for c in range(10)]
pt1,pt2 = [],[]
for m in mv:
    for sp in range(m[1]):
      t[0][0] += d[m[0]][0]
      t[0][1] += d[m[0]][1]
      for k in range(9):
        tm = md(t[k+1],t[k])
        t[k+1][0] += tm[0]
        t[k+1][1] += tm[1]
      if not t[1] in pt1:
          pt1.append(t[1][::])
      if not t[9] in pt2:
          pt2.append(t[9][::])
print 'part 1 -',len(pt1)
print 'part 2 -',len(pt2)
