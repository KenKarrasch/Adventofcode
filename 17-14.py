cd = open('17-14.txt').read()
d,sq,gr,r,s,g,bt,k = [[0,1],[1,0],[-1,0],[0,-1]],0,[],0,256,[],0,[]
l = nl = list(range(s))

def hash(f,l,num):
    sz,cp = 0,0    
    for d in range(num):
        l = l[(cp-s)%s:] + l[:(cp-s)%s]
        for i in f:    
            nl = l[:i%s][::-1] + l[i%s:]
            l = nl[(i+sz)%s:] + nl[:(i+sz)%s]     
            cp,sz = (cp+i+sz)%s,sz+1                                   
        l = l[(s-cp)%s:] + l[:(s-cp)%s]
    return(l)

for ct in range(128):
    inp = cd + '-' + str(ct)
    g,k,nsb = [],[],''   
    for i in inp: g.append(ord(i))
    g += [17, 31, 73, 47, 23]  
    l = hash(g,nl,64)
    for i in range(16):
        bt = 0
        for j in range(16): bt ^= l[(i*16)+j]
        k.append(bt)   
    for i in k:         
        bn = bin(i)[2:]
        bn = '0'*(8-len(bn)) + bn
        bn = bn.replace('0','.').replace('1','#')        
        nsb += bn    
    gr.append([i for i in nsb])    
    sq += nsb.count('#')    
print('part 1 -', sq)

def sqs(g):
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == '#': return True
    return False    
    
def inbd(x,y,ng):
    if x > -1 and x < 128 and y > -1 and y < 128: return wipe(x,y,ng)
    return ng

def wipe(x,y,g):        
    ng = g    
    if ng[x][y] == '#':
        ng[x][y] = '.'
        for o in [0,1,2,3]: ng = inbd(x+d[o][0],y+d[o][1],ng)        
    return ng

for x in range(128):
    for y in range(128):
        if gr[x][y] == '#': gr,r = wipe(x,y,gr),r+1
print('part 2 -',r) 
