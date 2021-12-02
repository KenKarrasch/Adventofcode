s = open('20-12.txt').read().split()
# Navigation puzzle
# Late start due to Christmas shopping
# part 1 - 13min solve, part 2 - 50min solve
# fumbled with part 2 getting my angles right, grade 9 math, all good fun
# made use of Rotation Matrix from Wikipedia
# learned about dictionaries in python

op,n = [],[]
for i in s:
    op.append(i[0][0])
    n.append(int(i[1:]))
x,y,d = 0,0,90
dr,xy = [[0,1],[1,0],[0,-1],[-1,0]],[0,0]
drs, b = {'N':[0,1],'S':[0,-1],'E':[1,0],'W':[-1,0]}, {'R':1,'L':-1}

for i in range(len(op)):
   if op[i] in 'NEWS': xy = [xy[w]+drs[op[i]][w]*n[i] for w in [0,1]]     
   if op[i] in 'RL': d += n[i]*b[op[i]]    
   if op[i] in 'F': xy = [xy[w]+n[i]*dr[int(d%360/90)][w] for w in [0,1]]

print('part 1 -',abs(xy[0])+abs(xy[1]))

def c(theta): return 1-(int((2*theta)/180)) if theta in [0,180] else 0 #cos
def s(theta): return 1-(2*int((theta-90)/180)) if theta in [90,270] else 0 #sin    
    
dx,dy,xy = 10,1,[0,0]
for i in range(len(op)):
    if op[i] in 'NEWS': dx, dy = dx+drs[op[i]][0]*n[i], dy+drs[op[i]][1]*n[i]
    if op[i] in 'RL':  
        th = n[i]*-b[op[i]]%360         
        dx,dy = dx*c(th)-dy*s(th),dx*s(th)+dy*c(th)        
    if op[i] in 'F': xy[0],xy[1] = xy[0]+dx*n[i], xy[1]+dy*n[i]
        
print('part 2 -',abs(xy[0])+abs(xy[1]))
