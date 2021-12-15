f = open('21-15test.txt').read().split('\n')
# Initially botched the modulo 9, it looked okay so I was debugging the 
# wrong part of my code. Very slow to compute, Will probably code it 
# in Java when I get a chance.

gr,b = [],[]
for i in f:
    r,br = [],[]    
    for u in i:
        r.append(int(u))
        br.append(100000000)
    gr.append(r)
    b.append(br)
bgr,bb = [],[]
sz = len(f)
if True:
 for bi in range(5*sz):
   r = []
   for bu in range(5*sz):
      r.append(100000000)
   bgr.append(r)
   bb.append(r[:])
 for tlx in range(5):
  for tly in range(5):
   for bi in range(sz):
    for bj in range(sz):      
      bgr[(tlx*sz)+bi][(tly*sz)+bj] = 1 + (-1 + gr[bi][bj] + (tlx+tly))%9

s = [[0,1],[1,0],[0,-1],[-1,0]]
b = [i[:] for i in bb]
gr = [i[:] for i in bgr]
sz = len(gr)
b[0][0] = 0

def gt(x,y):
    if -1 < x < sz and -1 < y < sz:
      return gr[x][y]
    return 100000000

ds,dn = 0,False
while not dn:
    ds += 1
    print(ds)    
    cl = []
    for i in range(sz):
      for j in range(sz):
        if b[i][j] == ds-1:
          for dx,dy in s:
             if not(dx == 0 and dy == 0):
              d = b[i][j] + gt(i+dx,j+dy)
              if d < 100000000:
               if d < b[i+dx][j+dy]:
                cl.append([i+dx,j+dy,d])                
                if i+dx == sz-1:
                  if j+dy == sz-1:                     
                     print( 'part 2',d)                     
                     dn = True
                if i+dx == (sz/5)-1:
                  if j+dy == (sz/5)-1:
                     pt1 = d
    for i in cl:
        b[i[0]][i[1]] = i[2]
print('part 1',pt1)
