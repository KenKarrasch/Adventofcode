f = open('day2in.txt').read().split('\n')

nf = ''
for i in f:
    nf = nf + i
f = nf.split(',')

sq = []
for i in f:
    st = int(i.split('-')[0])
    ed = int(i.split('-')[1])
    sq.append((st,ed+1))
so = ''

tly = 0
    
for i in sq:
    for s in range(i[0],i[1]):
        gd = True
        si = str(s)
        l = len(si)
        if l%2== 0:
            l2 = int(l/2)
            if si[0:l2] == si[l2:]:
                gd = False
        if not gd:
            tly += s
print(tly)
