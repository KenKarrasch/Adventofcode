f = open('21-11.txt').read().split('\n')
# Add 1s, get a list of octopuses flashes that have flashed, 
# redistribute, then see if any more octopuses have flashed, keep going
# until no more octopuses are flashing.
# Then do the nest round, etc
g,bn,fl = [],[],[0]
for i in f:
    rw = []
    rb = []
    for ch in i:
        rw.append(int(ch))
        rb.append(False)
    g.append(rw)
    bn.append(rb)

sx = len(g)
sy = len(g[0])

def gd(i,j):
    if  i > -1 and i < sx and j > -1 and j < sy: return True
    return False        

def inn(i,j):    
    for x in [-1,0,1]:
        for y in [-1,0,1]:            
            if not (y == 0 and x == 0):                                
                if gd(i+x,j+y):                        
                    g[j+y][i+x] += 1
def gns(nl):
    nb = [i[:] for i in nl]      
    for i in range(sx):
        for j in range(sy):
            if g[j][i] > 9:   
                if not bn[j][i]:
                    if [i,j] not in nb:               
                        nb.append([i,j])                        
    return nb

def dn():       
    ns = []
    for i in range(sx):
        for j in range(sy):
            g[j][i] += 1        
            bn[j][i] = False    
    ns = gns(ns)
    while len(ns) > 0:        
        inn(ns[-1][0],ns[-1][1])  
        bn[ns[-1][1]][ns[-1][0]] = True
        ns.pop()          
        ns = [i[:] for i in gns(ns)]                        
    lc = 0  
    for i in range(sx):
        for j in range(sy):
            if g[j][i] > 9:               
                g[j][i] = 0
                fl[0] += 1
                lc += 1
    if lc == 100: return True
    return False

done = False
t = 0
while not done:    
    if t == 100: print('part 1 -',fl[0])
    if dn():
            print('part 2 -',t+1)
            done = True
    t += 1
