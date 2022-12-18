f = open('22-18.txt').read().split('\n')

# Part 1 - Straightforward 13min solve.
# Part 2 - put the object in a bathtub, see where the water goes

q = []
dr = [[0,0, 1], [0, 1,0], [ 1,0,0],  [0,0,-1], [0,-1,0], [-1,0,0]] 

for i in f:
    im = i.split(',')
    cs = [int(x) for x in im]    
    l = []
    for s in cs:
        l.append(s)
    q.append(l)

cf = 0
mx,my,mz = [],[],[]

for c in q:    
    x,y,z = [k for k in c]    
    mx.append(x)
    my.append(y)
    mz.append(z)    
    for d in dr:
        i,j,k = x + d[0],y + d[1], z + d[2]
        if [i,j,k] in q:
            cf += 1

print('part 1 -',(6*len(q)) - cf)

nb = []
nq = [[max(mx)+1,0,0]]

while len(nq) > 0:       
   pl = nq.pop()
   x,y,z = pl[0],pl[1],pl[2]
   for d in dr:    
      i,j,k = x + d[0],y + d[1], z + d[2]      
      if (min(mx)-2 < i < max(mx)+2) and (min(my)-2 < j < max(my)+2) and (min(mz)-2 < k < max(mz)+2):        
        if [i,j,k] not in q:
          if [i,j,k] not in nb:                        
            nb.append([i,j,k])
            nq.append([i,j,k])
  

cf = 0
for c in q:    
    x,y,z = [k for k in c]    
    for d in dr:
        i,j,k = x + d[0],y + d[1], z + d[2]
        if [i,j,k] not in nb:
            cf += 1

print('part 2 -',(6*len(q)) - cf)
