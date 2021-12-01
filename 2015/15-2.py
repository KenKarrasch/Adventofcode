a,r,m = 0,0,[[0,2],[0,1],[1,2]]
for i in open('15-2.txt').read().split('\n'):
    b = [int(h) for h in i.split('x')]
    szs = []
    for j in m:
      a += 2*b[j[0]]*b[j[1]]
      szs.append(b[j[0]]*b[j[1]])
    a += min(szs)
    r += 2*(sum(b)-max(b))+b[0]*b[1]*b[2]
print 'part 1 -', a
print 'part 2 -', r
