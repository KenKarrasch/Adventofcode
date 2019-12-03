f = open('19-3.txt').read().split('\n')
# tried using a grid, ran out of memory. Tried calculating to each corner and then finding crossovers analytically, didn't work for all cases. 
#Ended up using sets, storing each step in memory.
u = [f[0].split(',')]
u.append(f[1].split(','))

w = [[1,0],[-1,0],[0,-1],[0,1]]#rlud
    
def gp(l):
    u,v,path,wd = 0,0,{},0
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
        wd += 1
        u += p[0]
        v += p[1]
        path[(u,v)] = wd
    return path

s1,s2 = gp(u[0]),gp(u[1])
btb = set(s1.keys())&set(s2.keys())

lst, lwd = [],[]
for (u,v) in btb:
   lst.append(abs(u)+abs(v))
for ind in btb:
   lwd.append(s1[ind]+s2[ind])
   
print 'part 1 -',min(lst)
print 'part 2 -',min(lwd)

