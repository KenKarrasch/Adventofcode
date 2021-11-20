import re

p,m,kl = open('17-20.txt').read().split('\n'),{},[]
e = range(len(p))

for i in e:
    st = p[i]
    m[i] = [int(i) for i in re.findall('[+-]?[0-9]+',st)]    

mn = {}
for i in e:
    mn[i] = sum([abs(j) for j in m[i][6:9]])
bk = min(mn, key=mn.get)
print('part 1 -',bk)
for c in range(100):        
    pl,plr = [],[]    
    for i in e:
        if i not in kl:        
            for dt in [3,0]: # calc v then p
                for d in [0,1,2]: # x,y,z
                    m[i][dt + d] += m[i][dt + 3 + d]             
                if dt == 0:
                    if m[i][0:3] not in pl:
                        pl.append(m[i][0:3])
                        plr.append(i)
                    else:
                        kl.append(i)
                        for q in range(len(pl)):
                            if m[i][0:3] == pl[q]:
                                if plr[q] not in kl:
                                    kl.append(plr[q])
print('part 2 -',len(m) - len(kl))
