import sys
import collections
import datetime

# Uses a basic Floodfill technique.
#
# It creates 200 empty mazes, one for each doughnut length, maze 0 is the top level maze.  At each empty space it 
# puts a 0 initially.
#
# At AA it puts a 1, then it searches each cell around that and puts a 2, then each cell around the 2's it puts 
# a 3 (if there is not already a number lower), and so on. When it reaches a portal it floods into the new maze at the 
# new different level. Eventually it snakes back to the top level ZZ.
#
# Did some optimisation of code to make it a little faster.  Keeps track of the maximum depth so know not to evaluate any deeper.
# Prepared a list of empty spaces, instead of searching every coordinate.
#
# It is acknowledged it could be done much, much faster using caching and a network, similar to day 18. 
#
# The trek from AA to ZZ takes 7658 steps.
# The number of doughnuts explored got to depth 120. The end was found it was exploring 2467 paths.
# Processing time was 1 min.

r = open('19-20.txt').read().split('\n')

def printgn(w,n):
 
 for li in range(len(w)):
  s = ''
  for c in range(len(w[li])):
    ch = w[li][c]
    if ch == '.':
      ch = '_'
      r = (li,c)
      if r in l:
        ch = l[r][0]
      if n[li][c] != 0:
        ch = str(n[li][c]%10)
    s += ch
  print(s)
  
def printg(w,n):
 for li in range(len(w)):
  s = ''
  for c in range(len(w[li])):
    ch = w[li][c]
    if ch == '.':
      ch = '_'
      r = (li,c)
    s += ch
  print(s)

def findl(r,szx,szy):
   l = {}
   st = end = (0,0)
   sz = szy
   uc = 'QWERTYUIOPASDFGHJKLZXCVBNM'
   m = 35 #38 to 97 = 49
   line = ''
   sz = min(szx,szy)
   for i in range(sz):
       #ken szx=133, szy=127 
       #dave szx=129, szy=135
     if True:
      if r[i][0]:
         s = r[i][0] + r[i][1]
         p = (i,2)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s
      if r[0][i]:
         s = r[0][i] + r[1][i]
         p = (2,i)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s
      if r[szy-1][i]:
         s = r[szy-2][i] + r[szy-1][i]
         p = (szy-3,i)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s
      if r[i][szx-2]:
         s = r[i][szx-2] + r[i][szx-1]
         p = (i,szx-3)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s 
     if (i > m) and (i < szy-m):
       if r[i][szx-(m+4)]:
         s = r[i][szx-(m+4)] + r[i][szx-(m+3)]
         p = (i,szx-(m+2))
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s
       if r[szy-(m+3)][i]:
         s = r[szy-m-4][i] + r[szy-m-3][i]
         p = (szy-m-2,i)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s
       if r[m+2][i]:
         s = r[m+2][i] + r[m+3][i]
         p = (m+1,i)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s
       if r[i][m-1]:
         s = r[i][m+2] + r[i][m+3]
         p = (i,m+1)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s 

   return l,st,end

def se(s,p,st,end):
    if s == 'AA':
        st = p
    if s == 'ZZ': end = p
    return(st,end)

def deadends(w):
    n = [[a[:] for a in g] for g in w]
    szx = len(w)
    szy = len(w[0])    
    done = False
    line = ''    
    m = [[0,1],[0,-1],[1,0],[-1,0]]
    while not done:
      done = True
      for x in range(szx-1):        
        for y in range(szy-1):
          ct = 0
          if n[x][y] == '.':
           ct = 0
           for d in m:
            tx,ty = x+d[0],y+d[1]
            if n[tx][ty] == '#':
              ct += 1
           if ct == 3:
            n[x][y] = '#'
            done = False
    return n

def inrange(x,y,sz):
    if (x > 0) and (x < sz) and (y > 0) and (y < sz):
        return True
    return False


def getnodes(n):
    for a in n:
        print (a)


szx = len(r[0])
szy = len(r)

print(szx,szy)

r = deadends(r)
printg(r,[])
l,st,end = findl(r,szx,szy)
print('l,st,end',l,st,end)

done = False
m = [[0,1],[0,-1],[1,0],[-1,0]]
depth = 1
n = [[0 for a in g] for g in r]

n[st[0]][st[1]] = 1

def edge(x,y,w,l,code):
    #dave 129,135 (132,126), ken 133,127 (124,130)
    if (x == 2) or (x == l-3) or \
       (y == 2) or (y == w-3):
        return -1 #outer edge
    else:        
        return 1 # inner edge

n = []
for a in range(200):
    mz = [[0 for a in g] for g in r]
    if a == 0:
        mz[st[0]][st[1]] = 1
    n.append(mz)

print(szx*szy)

print(datetime.datetime.now())

layer = [[st[0],st[1],0]]
mzmax = 2
mz = 0
layers = []
while not done:
   layers.append(len(layers))
   nlayer = []
   for ly in layer:
      mz = ly[2]
      cd = (ly[1],ly[0])
      if True:
          x = cd[1]
          y = cd[0]
          ni = n[mz]
          for s in [0,1,2,3]:          
            if r[x+m[s][0]][y+m[s][1]] == '.':
              ni = n[mz]  
              if ni[x+m[s][0]][y+m[s][1]] == 0:
                 ni[x+m[s][0]][y+m[s][1]] = depth+1
                 nlayer.append([x+m[s][0],y+m[s][1],mz])
          if (x,y) in l:            
            code = l[(x,y)]
            if (code == 'ZZ') and (mz == 0):
                printgn(r,n[0])
                print ('part 2 - ',depth-1)
                print ('maxdepth',mzmax)
                print('was exploring', len(layer),'paths when ZZ was found')
                print(datetime.datetime.now())                
                done = True
                break
                printgn(r,n)
            for a in l:
              if code == l[a]:
                if a != (x,y): 
                  e = edge(x,y,szx,szy,code)                
                  if  (e == 1):
                    if mzmax < mz+1:
                        mzmax = mz+1
                        #print('mzmax',mzmax,e,a,(x,y), szx,szy)
                    ni = n[mz+1]                   
                    ni[a[0]][a[1]] = depth+1                              
                    nlayer.append([a[0],a[1],mz+1])
                  if (mz != 0) and (e == -1):
                    ni = n[mz-1] 
                    ni[a[0]][a[1]] = depth+1                              
                    nlayer.append([a[0],a[1],mz-1])
                    
   if depth % 1000 == 0:
       for mzn in range(3):
           print('depth',depth)
           print('doughnut',mzn)
           print('exploring', len(layer),'paths')
           printgn(r,n[mzn])
   depth += 1
   layer = []
   for nl in nlayer: layer.append(nl)
