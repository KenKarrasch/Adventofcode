fn = open("17-7.txt").read().split('\n')
nw,f = -1,[]
for i in fn:
    b = []
    for j in i.split():
        if '(' in j:
            b.append(int(j[1:-1]))
        else:
            b.append(j.replace(',',''))
    if len(b) > 2:
        l = []
        for j in range(len(b)-3):
            l.append(-1)
        b.append(l)
    f.append(b)
for i in range(len(f)):
    if len(f[i]) > 2:
        for h in range(len(f[i][-1])):            
            for y in range(len(f)):
                if f[y][0] == f[i][h+3]:
                    f[i][-1][h] = y

st = -1
for i in range(len(f)):
    top = True    
    r = f[i][:]
    if len(r) < 3:
        top = False
    for j in f:        
        if j != f[i]:         
            if r[0] in j:                                                
                top = False        
    if top:
        st = i
        print('part 1 -',r[0])

def chkw(d):    
    if len(f[d]) == 2: return f[d][1]        
    w = []        
    for i in f[d][-1]:
        w.append(chkw(i))            
    if -1 in w: return -1
    if min(w) != max(w):
        nwts = w[:]        
        nwts.sort()
        stw,ct,r = nwts[0],0,-1
        for p in w:
            if stw == p: ct += 1
        if ct == 1: o = stw
        else: o = nwts[-1]        
        for e in range(len(w)):
            if w[e] == o: r = e                
        nw = f[f[d][-1][r]][1] + (min(w)-max(w)) * (1-2*(o != max(w)))                   
        if nw != -1:
            print('part 2 -',nw)                            
            return -1        
    return f[d][1] + sum(w)    
chkw(st)
