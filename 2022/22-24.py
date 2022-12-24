
from collections import defaultdict, deque
f = open('22-24.txt').read().split('\n')

#  Similar to day 18,  calculate if a square is safe by taking modulus of position plus time
#  BFS, use DP to remove lines already explored.
#
#  Part 2, cut and paste three ways

   
gr = []


dr = [(-1,0),(0,1),(1,0),(0,-1),(0,0)]

for i in range(1,len(f)-1):
    ln = []
    for b in range(1,len(f[i])-1):
      ln.append(f[i][b])
    gr.append(ln)

hp = len(gr[0])
vp = len(gr)

bl = {}

for y in range(len(gr)):
  for x in range(len(gr[y])):
     if gr[y][x] != '.':
       bl[(x,y)] = gr[y][x]

def blz(x,y,t):  
     ht = False     
     blk = bl.keys()
     blzs = 0
     if (x,(y+t)%vp) in blk:        
        if bl[(x,(y+t)%vp)] == '^':             
            blzs += 1
     if (x,(y-t)%vp) in blk:         
        if bl[(x,(y-t)%vp)] == 'v':             
            blzs += 1
     if ((x+t)%hp,y) in blk:                
        if bl[((x+t)%hp,y)] == '<':             
            blzs += 1
     if ((x-t)%hp,y) in blk:        
        if bl[((x-t)%hp,y)] == '>':             
            blzs += 1
     if blzs > 0:
        return True
     return False    

q = deque([(0,-1,0,'')]) # x,y,t

dst = (hp-1,vp)

DP = set()

done = False
while q and not done:
    x,y,t,pth = q.popleft()
    if (x,y,t) in DP:
        continue
    DP.add((x,y,t))
    if (x,y) == (hp,vp+1):
        bst = min(bst,t)
    if blz(x,y,t):       
       continue 
    else:
      for d in dr: 
        nx = x + d[0]
        ny = y + d[1]
        if (nx,ny) == (dst[0],dst[1]):                    
          print('part 1 -',t+1)          
          done = True
          break
        if nx < hp and ny < vp:
         if (nx >= 0 and ny >= 0) or ((nx == 0) and (ny == -1)):
           q.append((nx,ny,t+1,''))

# Go home
q = deque([(hp-1,vp,t+1,'')]) # x,y,t
dst = (0,-1)
done = False
while q and not done:
    x,y,t,pth = q.popleft()
    if (x,y,t) in DP:
        continue
    DP.add((x,y,t))
    if (x,y) == (hp,vp+1):
        bst = min(bst,t)
    if blz(x,y,t):       
       continue 
    else:
      for d in dr: 
        nx = x + d[0] 
        ny = y + d[1]
        if (nx,ny) == (dst[0],dst[1]):                    
          print('home -',t+1)          
          done = True
          break
        if nx < hp and ny < vp:
         if (nx >= 0 and ny >= 0) or ((nx == hp-1) and (ny == vp)):
           q.append((nx,ny,t+1,''))

# go again
q = deque([(0,-1,t+1,'')]) # x,y,t
dst = (hp-1,vp)
done = False
while q and not done:
    x,y,t,pth = q.popleft()
    if (x,y,t) in DP:
        continue
    DP.add((x,y,t))
    if (x,y) == (hp,vp+1):
        bst = min(bst,t)
    if blz(x,y,t):       
       continue 
    else:
      for d in dr: 
        nx = x + d[0]
        ny = y + d[1]
        if (nx,ny) == (dst[0],dst[1]):                    
          print('part 2 -',t+1)          
          done = True
          break
        if nx < hp and ny < vp:
         if (nx >= 0 and ny >= 0) or ((nx == 0) and (ny == -1)):
           q.append((nx,ny,t+1,''))
