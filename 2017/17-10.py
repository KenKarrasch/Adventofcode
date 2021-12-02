inp = open('17-10.txt').read()
f,s,g,bt,k,ns = [int(i) for i in inp.split(',')],256,[],0,[],''
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
        
l = hash(f,l,1)
print('part 1 -',l[0] * l[1])
for i in inp: g.append(ord(i))
g += [17, 31, 73, 47, 23]
l = hash(g,nl,64)  
for i in range(16):    
    bt = 0
    for j in range(16): bt ^= l[(i*16)+j]
    k.append(bt)
for i in k: ns += hex(i)[2:]
print('part 2 -',ns)
