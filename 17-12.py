f,en,ct = [i.replace(',',' ').replace('<->','') for i in open('17-12.txt').read().split('\n')],[],1
for j in f: en.append([i for i in j.split()])

def getgr(st,f):
    gp,dn = {st:0},False    
    while not dn:
        dn = True
        for i in f:      
            k = list(gp.keys())        
            for el in i:        
                if el in k:
                    for p in i:
                        if p not in k: 
                            gp[p] = 0  
                            dn = False      
    return(gp)

def remlist(gs,f):
    nf = []
    for i in f:
        dn = False
        for g in gs:
            if g in i: dn = True
        if not dn: nf.append(i)
    return nf

gp = getgr('0',en)
print('part 1 -', len(gp))
nf = remlist(list(gp.keys()),en)
while len(nf) > 0:    
    gp = getgr(nf[0][0],nf)    
    nf,ct = remlist(list(gp.keys()),nf),ct+1
print('part 2 -',ct)
