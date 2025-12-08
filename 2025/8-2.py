f = [[int(x) for x in y.split(',')] for y in open('25-8.txt').read().split('\n')]
# 8    7269    920  ***

pr = []

print('calculating distances')

for i in range(len(f)):
    for j in range(i+1,len(f)):        
        dl = (f[i][0]-f[j][0]) * (f[i][0]-f[j][0]) 
        dl += (f[i][1]-f[j][1]) * (f[i][1]-f[j][1])
        dl += (f[i][2]-f[j][2]) * (f[i][2]-f[j][2])       
        pr.append((dl, i,j))

pr.sort()

print('finding best span')

bxc = []
dn = False
p = 0
gr = []
while not dn:
    i = pr[p]
    p += 1    
    b1 = (f[i[1]][0],f[i[1]][1],f[i[1]][2])
    b2 = (f[i[2]][0],f[i[2]][1],f[i[2]][2])    
    if b1 not in bxc:
        bxc.append(b1)
    if b2 not in bxc:
        bxc.append(b2)

    g1 = -1
    g2 = -1
    for g in range(len(gr)):
        if b1 in gr[g]:            
            g1 = g
        if b2 in gr[g]:    
            g2 = g
    if g1 != -1 and g2 != -1:
        if g1 != g2:
            merge = gr[g1] + gr[g2]
            gr[g1] = merge
            del gr[g2]           
    if g1 == -1 and g2 != -1:
        gr[g2] = gr[g2] + [b1]    
    if g1 != -1 and g2 == -1:
        gr[g1] = gr[g1] + [b2]            
    if g1 == -1 and g2 == -1:
        gr.append([b1] + [b2])

    if len(bxc) == len(f) and len(gr) == 1:
        dn = True
        print(b1[0]*b2[0])
