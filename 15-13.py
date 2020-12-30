import math
ns = open('15-13.txt').read().split('\n')
book = []
names = []
maxh = []

def gethapna(i,j):
    for a in book[i]:
        if a[1] == j:
          return(a[2])        

def gethapn(seating):
    hap = 0    
    for i in range(sq+1):
        s1 = seating[i]
        s2 = seating[(i+1)%(sq+1)]
        hap += gethapna(s1,s2)
        hap += gethapna(s2,s1)
    return hap

def gethap(seating,sq,depth):
    if depth != 0:
        seats = range(sq+1)
    else: seats = [0]
    if len(seating) < sq+1:
        for i in seats:
            if i not in seating:
                gethap(seating[:] + [i],sq,depth+1)                        
    else:        
        maxh.append(gethapn(seating))

p = 0
sq = math.floor(math.sqrt(len(ns)))

names = {}

for i in range(sq+1):
    names[ns[i*sq].split()[0]] = i

for i in range(sq+1):
    pers = []
    for j in range(sq):        
        neg = 1
        if 'lose' in ns[p]:
            neg = -1
        amt = neg*int(ns[p].split()[3])
        pers.append([names[ns[p].split()[0]],names[ns[p].split()[10][0:-1]],amt])
        p += 1
    book.append(pers)

gethap([],sq,0)
print('part 1 -',max(maxh))

names['me'] = len(names)
book = []
p = 0
for i in range(sq+1):    
    pers = [[names[ns[p].split()[0]],names['me'],0]]
    for j in range(sq):
        neg = 1
        if 'lose' in ns[p]:
            neg = -1
        amt = neg*int(ns[p].split()[3])
        pers.append([names[ns[p].split()[0]],names[ns[p].split()[10][0:-1]],amt])
        p += 1    
    book.append(pers)
pers = []
for i in range(sq+1):    
    pers.append([names['me'],names[ns[i*sq].split()[0]],0])
book.append(pers)
sq += 1    
maxh  = []
gethap([],sq,0)
print('part 2 -',max(maxh))
