f = [[int(x) for x in y.split(',')] for y in open('25-8.txt').read().split('\n')]
#  8    7105    904  ***
# 51 mins

pr = []

for i in range(len(f)):
    for j in range(i,len(f)):
        if i != j:
            dl = (f[i][0]-f[j][0]) * (f[i][0]-f[j][0]) 
            dl += (f[i][1]-f[j][1]) * (f[i][1]-f[j][1])
            dl += (f[i][2]-f[j][2]) * (f[i][2]-f[j][2])            
            pr.append((dl, i,j))

pr.sort()
bxc = []
cns = {}

for i in pr[0:1000]: 
    b1 = (f[i[1]][0],f[i[1]][1],f[i[1]][2])
    b2 = (f[i[2]][0],f[i[2]][1],f[i[2]][2])
    if b1 not in bxc:
        bxc.append(b1)
    if b2 not in bxc:
        bxc.append(b2)
    if b1 in cns:
        cns[b1] = cns[b1] + [b2]
    else:
        cns[b1] = [b2]
    if b2 in cns:
        cns[b2] = cns[b2] + [b1]
    else:
        cns[b2] = [b1]
    

cl = []

def exp(bx,pth):        
    for i in cns[bx]:
        if i not in pth:     
            if i not in cl:
                cl.append(i)   
            exp(i,pth + [i])    

sz = []
seen = []

for b in bxc:    
    if b not in seen:
        cl = [b]        
        exp(b,[])
        for i in cl:
            if i not in seen:
                seen.append(i)                
        sz.append(len(cl))

sz.sort(reverse=True)
ml = 1
for i in sz[0:3]:
    ml *= i
print(ml)
