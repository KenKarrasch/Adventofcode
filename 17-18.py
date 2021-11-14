c,r,r0,r1 = [i.split() for i in open('17-18.txt').read().split('\n')],{},{},{}
lt = 'qwertyuiopasdfghjklzxcvbnm'

def gv(v):
    if v in lt:
        return r[v]
    return int(v)

for h in c: #Set all known registers to zero
    if h[1] in lt:
        r[h[1]] = 0
        r0[h[1]] = 0
        r1[h[1]] = 0
    if len(h) > 2:
        if h[2] in lt:
            r[h[1]] = 0
            r0[h[1]] = 0
            r1[h[1]] = 0

f,ls,rf,dn = 0,-1,-1,False
while f < len(c) and not dn:
    i = c[f]
    if i[0] == 'snd': ls = gv(i[1])
    if i[0] == 'add': r[i[1]] += gv(i[2])
    if i[0] == 'mul': r[i[1]] *= gv(i[2])
    if i[0] == 'mod': r[i[1]] %= gv(i[2])
    if i[0] == 'set': r[i[1]] = gv(i[2])
    if i[0] == 'jgz':
        if gv(i[1]) > 0: f = f+gv(i[2])-1            
    if i[0] == 'rcv':
        if gv(i[1]) > 0:            
            rf = ls            
            dn = True
    f += 1    
print('part 1 -',rf)    

def gv1(r,v):
    if v in lt:
        return r[v]
    return int(v)

def domusic(r,f,ix,c):                
    sq = []           
    while f < len(c):
        i = c[f]        
        if i[0] == 'snd': sq.append(gv1(r,i[1]))            
        if i[0] == 'add': r[i[1]] += gv1(r,i[2])
        if i[0] == 'mul': r[i[1]] *= gv1(r,i[2])
        if i[0] == 'mod': r[i[1]] %= gv1(r,i[2])
        if i[0] == 'set': r[i[1]] = gv1(r,i[2])
        if i[0] == 'jgz':
            if gv1(r,i[1]) > 0: f = f+gv1(r,i[2])-1            
        if i[0] == 'rcv':
            if len(ix) == 0: return f,sq           
            r[i[1]] = ix[0]
            ix = ix[1:]            
        f += 1         

r0,r1,f,ix,ct,sq = {},{},[0,0],[],0,[]
r0['p'],r1['p'] = 0,1
while True:
    f[0],ix = domusic(r0,f[0],ix,c)    
    f[1],ix = domusic(r1,f[1],ix,c)    
    if len(ix) == 0: break
    ct += len(ix)
print('part 2 -',ct)
