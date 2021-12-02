r = open('20-2.txt').read().split('\n')

mn,mx,l,st = [],[],[],[]

for g in r:
    h = g.split()
    ls = h[0].split('-')
    mn.append(int(ls[0]))
    mx.append(int(ls[1]))
    l.append(h[1][:-1])
    st.append(h[2])
    
vp = 0
for i in range(len(mn)):
    ct = 0
    for h in st[i]:
        if h == l[i]:
           ct += 1
    if (ct > mn[i]-1):
        if (ct < mx[i]+1):
            vp += 1
print 'part 1 -', vp

vp = 0
for i in range(len(mn)):
    ct = 0
    if st[i][mn[i]-1] == l[i]:
      ct += 1
    if st[i][mx[i]-1] == l[i]:
      ct += 1
    if ct == 1:
       vp += 1
print 'part 2 -', vp
