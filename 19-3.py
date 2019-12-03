f = open('19-3.txt').read().split('\n')
# tried using a grid, ran out of memory. Tried calculating analytically, didn't work for all cases. 
#Ended up using sets, storing each step in memory.
u = [f[0].split(',')]
u.append(f[1].split(','))

w = [[1,0],[-1,0],[0,-1],[0,1]]#rlud
    
def gp(l):
    x,y = 0,0
    path = {}
    wd = 0
    for d in l:
      p = [0,0]
      if 'R' in d:
       p = w[0]
      if 'L' in d:
       p = w[1]
      if 'U' in d:
       p = w[2]
      if 'D' in d:
       p = w[3]
      for _ in range(int(d[1:])):
        x += p[0]
        y += p[1]
        wd += 1
        if (x,y) not in path:
          path[(x,y)] = wd
    return path

sa = gp(u[0])
sb = gp(u[1])
btb = set(sa.keys())&set(sb.keys())

lst = []
lwd = []
for (x,y) in btb:
   lst.append(abs(x)+abs(y))
for ind in btb:
   lwd.append(sa[ind]+sb[ind])
   
print 'part 1 -',min(lst)
print 'part 2 -',min(lwd)

