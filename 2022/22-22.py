import re

f = open('22-22.txt').read().split('\n')

# Not a general solution, hard coded the edges, Will make a general solution after Christmas

# Fun cube puzzle

mz = []
ln = len(f[0])
for i in f:
  if ('#' in i) or \
     ('.' in i) or \
     (' ' in i):
       l = []
       for ch in i:
          l.append(ch)       
       if len(i) < ln:
         for i in range(ln-len(i)):
            l.append(' ')
       mz.append(l)
inst = f[-1]

x = y = 0
cd = 0

dr = [(1,0),(0,1),
     (-1,0),(0,-1)]
u = ['>','v','<','^']

inst = inst.replace('R',',R,')
inst = inst.replace('L',',L,')
tok = inst.split(',')
t = []
for i in tok:
  if i in 'RL':
    t.append(i)
  else:  
    t.append(int(i))
 

def pr():
    for i in mz:
      st = ''      
      for j in i:
        st += j
      print (st)
    print()
    
sqr = [[(50,99),(0,49)],[(100,149),(0,49)],[(50,99),(50,99)],[(0,49),(100,149)],[(50,99),(100,149)],[(0,49),(150,199)]] 
dm = {(0,3): 0, (0,5): 0, (1,2): 2, (1,4): 2, (1,5): 3, (2,1): 3, (2,3): 1, (3,0): 0, (3,2): 0, (4,1): 2, (4,5): 2, (5,0): 1, (5,1): 1, (5,4): 3}

nf = [[1,2,3,5],[4,2,0,5],[1,4,3,0],[4,5,0,2],[1,5,3,2],[4,1,0,3]]
'''
sqr = [[(8,11),(0,3)],[(0,3),(4,7)],[(4,7),(4,7)],[(8,11),(4,7)],[(8,11),(8,11)],[(12,15),(8,11)]] 
dm = {(0,1): 1, (0,2): 1, (0,5): 2, (1,0): 2, (1,4): 3, (1,6): 3, (2,0): 0, (2,4): 0, (3,5): 1, (4,2): 3, (4,1): 3, (5,3): 2, (5,0): 2, (5,2): 0}

nf = [[5,3,2,1],[2,4,5,0],[3,4,1,0],[5,4,2,0],[5,1,2,3],[0,1,4,3]]
'''

def getface(x,y):
  for fc in range(len(sqr)):
    if sqr[fc][0][0] <= x <= sqr[fc][0][1]:
      if sqr[fc][1][0] <= y <= sqr[fc][1][1]:
        return fc
  return None

def facechange(x,y,xx,yy,cd):  
   nx = x + xx
   ny = y + yy
   f1 = getface(x,y)
   f2 = nf[f1][cd]
   ncd = cd      
   if getface(nx,ny) != f1:            
      if (f1,f2) in dm.keys():
        face = sqr[f1]
        if cd == 0: dist = y - face[1][0]
        if cd == 1: dist = face[0][1] - x
        if cd == 2: dist = face[1][1] - y
        if cd == 3: dist = x - face[0][0]      
        ncd = dm[(f1,f2)]        
        face = sqr[f2]
        if ncd == 0:          
          ny = face[1][0] + dist
          nx = face[0][0]
        if ncd == 1:          
          ny = face[1][0] 
          nx = face[0][1] - dist
        if ncd == 2:          
          ny = face[1][1] - dist
          nx = face[0][1]
        if ncd == 3:                    
          ny = face[1][1]
          nx = face[0][0] + dist             
   return (ncd,nx,ny,dr[ncd][0],dr[ncd][1])


for i in t:
    ox = x
    oy = y
    if i == 'R':
      cd = (cd+1)%4
      mz[y][x] = u[cd]
    if i == 'L':
      cd = (cd-1)%4
      mz[y][x] = u[cd]
    if type(i) == type(1):
      xx,yy = dr[cd]
      for p in range(i):
        if mz[(y+yy)%len(mz)] \
         [(x+xx)%len(mz[0])] != '#':
          mz[y][x] = u[cd]
          x += xx
          y += yy
          x = x%len(mz[0])
          y = y%len(mz)
          if mz[y][x] == ' ':
           ex,ey = x,y
           while (mz[ey][ex] == ' '):
            ex += xx
            ey += yy
            ex = ex%len(mz[0])
            ey = ey%len(mz)
           if mz[ey][ex] != '#':
             x = ex
             y = ey
           else:
             x = (x-xx)%len(mz[0])
             y = (y-yy)%len(mz)        


for i in t:
    ox = x
    oy = y
    if i == 'R':
      cd = (cd+1)%4
      mz[y][x] = u[cd]
    if i == 'L':
      cd = (cd-1)%4
      mz[y][x] = u[cd]
    if type(i) == type(1):
      xx,yy = dr[cd]
      for p in range(i):
        if mz[(y+yy)%len(mz)] \
         [(x+xx)%len(mz[0])] != '#':
          mz[y][x] = u[cd]
          x += xx
          y += yy
          x = x%len(mz[0])
          y = y%len(mz)
          if mz[y][x] == ' ':
           ex,ey = x,y
           while (mz[ey][ex] == ' '):
            ex += xx
            ey += yy
            ex = ex%len(mz[0])
            ey = ey%len(mz)
           if mz[ey][ex] != '#':
             x = ex
             y = ey
           else:
             x = (x-xx)%len(mz[0])
             y = (y-yy)%len(mz)        

print('part 1 -',(y+1)*1000 + (1+x)*4 + cd)

x = 50
y = 0

for i in t:
    if i == 'R':
      cd = (cd+1)%4
      mz[y][x] = u[cd]
    if i == 'L':
      cd = (cd-1)%4
      mz[y][x] = u[cd]
    if type(i) == type(1):
      xx,yy = dr[cd]
      for p in range(i):    
        if y == -1:
          print('rot')
        px,py,pcd,pxx,pyy = x,y,cd,xx,yy        
        cd,x,y,xx,yy = facechange(x,y,xx,yy,cd)
        ch = mz[y][x]
        if mz[y][x] != '#':
          mz[y][x] = u[cd] 
        else: 
          x,y,cd,xx,yy = px,py,pcd,pxx,pyy  
          continue
    #pr()
print('part 2 -',(y+1)*1000 + (1+x)*4 + cd)


# 123149
