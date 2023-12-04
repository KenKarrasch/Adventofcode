r = open('23-4.txt').read().split('\n')

pt1,cw,st,cdn = 0,[],[],0
for i in range(len(r)):
    st.append(0)
for cd in r:
    cdn += 1
    wn = cd.split('|')[0].split(':')[1].split()
    gs = cd.split('|')[1].split()
    wns,dbl = 0,1
    for i in wn:
        if i in gs:
            wns +=1
            dbl *= 2
    pt1 += dbl/2
    cds = []
    st[cdn-1] += 1
    for i in range(wns):
        cds.append(cdn+1+i)
    cw.append(cds)
for i in range(len(r))[::-1]:
    for ws in cw[i]:
        st[i] += st[ws-1]
print 'part 1',pt1
print 'part 2',sum(st)
