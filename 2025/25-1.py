f = open('25-12-1.txt').read().split('\n\n')

# 12   10732   3070  ****

sq = []

for i in f[0:-1]:
    ct = 0
    for c in i:
        if c == '#':
            ct += 1
    sq.append(ct)

ct = 0
rs = []
for i in f[-1].split('\n'):    
    #print(i.split(':')[0].split('x'))
    mt = i.split(':')[0].split('x')
    #print(mt)
    m = 1
    for rf in range(len(mt)):
        m *= int(mt[rf])
    #print(m)
    ssq = 0
    for rf,pt in enumerate(i.split(':')[1].split()):
        ssq += sq[rf]*int(pt)    
    print(m,ssq, ssq/m)
    rs.append(ssq/m) 
    if ssq/m < 1:
        ct += 1
rs.sort()
for r in rs:
    print(r)
print (sq)
print(len(f[-1].split('\n')))
print(ct)
