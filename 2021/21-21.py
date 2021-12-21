f = open('21-21.txt').read().split('\n')

# good problem for dp

p = [int(i[-1]) for i in f]

sp = p[:]
a = 1
lst = []
sc = [0,0]
dn = [False]

def ds(pl,a):
    lst = sc[:]
    sc[pl] += sp[pl]
    if max(sc) > 999:
      if not dn[0]:
       print 'part 1 -',min(sc)*(a-1)
       dn[0] = True
    
while max(sc) < 1000:
    for i in [0,1]:
       for b in [0,1,2]:
           sp[i] += a
           a += 1
       sp[i] = ((sp[i]-1)%10)+1
       ds(i,a)

dp = {}

ot = []
for i in [1,2,3]:
  for j in [1,2,3]:
    for k in [1,2,3]:
        ot.append(i+j+k)

def do(pl,s0,s1,p0,p1):
    if (pl,s0,s1,p0,p1) in dp:
        return dp[(pl,s0,s1,p0,p1)]
    p0n = p0
    p1n = p1
    if s0 > 20: return [1,0]
    if s1 > 20: return [0,1]
    g = []
    if pl == 0:
      for i in ot:
        p0n = ((p0+i-1)%10)+1
        g.append(do(1, \
        s0+p0n,s1,p0n,p1n))
    if pl == 1:
      for i in ot:
        p1n = ((p1+i-1)%10)+1
        g.append(do(0,\
        s0,s1+p1n,p0n,p1n))
    t0 = 0
    t1 = 0
    for i in g:
       t0 += i[0]
       t1 += i[1]
    dp[(pl,s0,s1,p0,p1)] = [t0,t1]
    return [t0,t1]
      
print 'part 2 -',max(do(0,0,0,p[0],p[1]))
