f = open('25-5test.txt').read().split('\n\n')

# overlaps and edge cases
# 5    6906   3924  ****

ig = [int(x) for x in f[1].split('\n')]
iri = [x.split('-') for x in f[0].split('\n')]
ir = []

for h in iri:
    ir.append((int(h[0]),int(h[1])))

def merge(r,ra,mx):
    ran = ra[:]   
    free = []
    if len(ra) == 0:
        free.append((0,mx))
    else:
        free = [(0,ra[0][0]-1),(ra[-1][1]+1,mx)]
        for i in range(len(ra)-1):                        
            free.append((ra[i][1]+1,ra[i+1][0]-1))    
    free.sort()
    for i in free:
        if r[0] <= i[0] and r[1] > i[1]: # completely covers area            
            ran.append((i[0],i[1]))            
        if r[0] > i[0] and r[1] <= i[1]: # completely within area            
            ran.append((r[0],r[1]))            
        if r[0] > i[0] and r[0] < i[1] and r[1] > i[1]:            
            ran.append((r[0],i[1]))  # top end            
        if r[0] <= i[0] and r[1] < i[1] and r[1] > i[0]:            
            ran.append((i[0],r[1]))  # bottom end            
    ran.sort()    
    return(ran)

ir.sort()

mx = 0
for i in ir:    
    if i[1] > mx:
        mx = i[1]
ran = []
for i in ir:
    ran = merge(i,ran,mx+1)
tly = 0
for i in ran:
    tly += 1 + i[1]-i[0]

print(tly+4)
