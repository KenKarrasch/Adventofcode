r = open('23-2.txt').read().split('\n')

cls, lm = ['red','green','blue'],[12,13,14]

def count(g,color):    
    cs = g.split(',')
    for c in cs:
        if color in c:
            return int(c.split()[0])
    return 0
    
pt1 = pt2 = 0
for g in range(len(r)):    
    gss = r[g].split(':')[1].split(';')        
    tm, mxs, p = False, [0,0,0], 1    
    for gm in gss:
        for cl in range(3):
            if mxs[cl] < count(gm,cls[cl]):
                mxs[cl] = count(gm,cls[cl])                      
            if count(gm,cls[cl]) > lm[cl]:
                tm = True          
    for cl in range(3): p *= mxs[cl]            
    pt2 += p
    if not tm:
        pt1 += g + 1

print ('part 1:',pt1)
print ('part 2:',pt2)
