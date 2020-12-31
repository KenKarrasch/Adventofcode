import math
ns = open('15-15.txt').read().split('\n')
ing,maxp1,maxp2 = [],[],[]

def gethapn(am):
    gd = 1
    for i in range(len(ing[0])-1):
        bt = 0
        for j in range(len(am)):            
            bt += ing[j][i]*am[j]
        if bt < 0:
                return 0,0
        gd *= bt
    cal = 0
    for j in range(len(am)):            
        cal += ing[j][len(ing[0])-1]*am[j]
    return gd,cal

def gethap(am,maxq,depth,sz):
    amt = am[:]
    if sum(am) > maxq:
        return -1000000
    if depth == 0:
        amt[0] = 100
        for l in range(1,sz):            
            amt[0] -= amt[l]
        vl,cal = gethapn(amt)
        maxp1.append([vl,amt])
        if cal == 500:
            maxp2.append([vl,amt])
        return 0
    for i in range(maxq):
        amt[depth] = i
        gethap(amt,maxq,depth-1,sz)    

for k in ns:
    i = k.split(',')
    ingr = [int(i[0].split()[2]),int(i[1].split()[1]),int(i[2].split()[1]),
            int(i[3].split()[1]),int(i[4].split()[1])]
    ing.append(ingr)
sz = len(ing)
am = [0 for i in range(sz)]
gethap(am,100,sz-1,sz)
print('part 1 -',max(maxp1)[0])
print('part 1 -',max(maxp2)[0])
