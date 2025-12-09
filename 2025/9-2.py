f = [y for y in open('25-9.txt').read().split('\n')]
# 9    6767  15944  ******

# Lots of jumbling about the limits and intersections until it worked
# Technically not a general solution, relies on Only two coordinates share the same 
# line vertically or horizontally, and coordinates must be two or more apart

# Also, borrowed the line intersect code from my Everybody codes, solution day 15, "Ducks and Dragons", worked a treat

nf = []

for i in f:
    pr = [int(x) for x in i.split(',')]
    nf.append((pr[0],pr[1]))

nf.sort()
f = nf

def lms(p, q, r,touch):
    if touch:
        return (min(p[0], r[0]) < q[0] < max(p[0], r[0]) and
                min(p[1], r[1]) < q[1] < max(p[1], r[1]))
    else:
        return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def ont(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  
    return 1 if val > 0 else 2  


def intersect(p1, q1, p2, q2,touch):
    o1 = ont(p1, q1, p2)
    o2 = ont(p1, q1, q2)
    o3 = ont(p2, q2, p1)
    o4 = ont(p2, q2, q1)
    
    if (o1 != o2) and (o3 != o4):
        return True

    if o1 == 0 and lms(p1, p2, q1,touch): return True
    if o2 == 0 and lms(p1, q2, q1,touch): return True
    if o3 == 0 and lms(p2, p1, q2,touch): return True
    if o4 == 0 and lms(p2, q1, q2,touch): return True

    return False

pr = []

for p1 in range(len(f)):
    for p2 in range(p1+1, len(f)):
        if f[p1][0] == f[p2][0]:
            pr.append(((f[p1][0],f[p1][1]),(f[p2][0],f[p2][1])))
        if f[p1][1] == f[p2][1]:
            pr.append(((f[p1][0],f[p1][1]),(f[p2][0],f[p2][1])))

szs = []

for p1 in range(len(f)):    
    print(p1)
    for p2 in range(p1+1, len(f)):
        gd = True
        for p in pr:            
            if f[p1] != p[0] and f[p1] != p[1] and f[p2] != p[0] and f[p2] != p[1]:
                if intersect(f[p1],f[p2],p[0],p[1],False):    
                    gd = False
        if gd:
            if f[p1][1] < f[p2][1]:
                le = ((0,f[p1][1]+1), (f[p1][0]+1,f[p1][1]+1))           
            else:
                le = ((0,f[p1][1]-1), (f[p1][0]+1,f[p1][1]-1))                       
            ct = 0           
            for p in pr:                        
                if intersect(le[0],le[1],p[0],p[1],False):               
                    ct += 1
            for pt in f:
                if pt != p1 and pt != p2:
                    if f[p1][1] < f[p2][1]:    
                        if pt[0] > f[p1][0] and pt[0] < f[p2][0] and pt[1] > f[p1][1] and pt[1] < f[p2][1]:
                            gd = False
                    else:
                        if pt[0] > f[p1][0] and pt[0] < f[p2][0] and pt[1] < f[p1][1] and pt[1] > f[p2][1]:
                            gd = False

            if ct%2!=1:
                gd = False     

            if gd:
                sz = (1+abs(f[p1][0]-f[p2][0])) * (1+abs(f[p1][1]-f[p2][1]))
                szs.append((sz,f[p1],f[p2]))

print(max(szs)[0])
