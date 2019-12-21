import sys
import collections
# part 2 only
r = open('19-20.txt').read().split('\n')

# Straightforward extension of part 1

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

def findl(r):
   l = {}
   sz = len(r)
   st = end = (0,0)
   uc = 'QWERTYUIOPASDFGHJKLZXCVBNM'
   d = [[0,1],[sz,sz-1,sz-2]]
   m = 35
   line = ''
   for i in range(sz):
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
      if r[sz-1][i]:
         s = r[sz-2][i] + r[sz-1][i]
         p = (sz-3,i)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s
      #line += r[i][sz+4]
      if r[i][sz+4]:
         s = r[i][sz+4] + r[i][sz+5]
         p = (i,sz+3)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s 
     if (i > m) and (i < sz-m):
       if r[i][2+sz-m]:
         s = r[i][2+sz-m] + r[i][3+sz-m]
         p = (i,4+sz-m)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s
       if r[sz-m+1][i]:
         s = r[sz-m-4][i] + r[sz-m-3][i]
         p = (sz-m-2,i)
         st,end = se(s,p,st,end)
         if s[0] in uc: l[p] = s
       if r[m-1][i]:
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


szx = len(r[0])
szy = len(r)

r = deadends(r)
l,st,end = findl(r)

done = False
m = [[0,1],[0,-1],[1,0],[-1,0]]
depth = 1
codef = False
n = [[0 for a in g] for g in r]
n[st[0]][st[1]] = 1
    
def edge(x,y,szx,szy):
    if (x == 2) or (x == szx-9) or \
       (y == 2) or (y == szy+3):
        return -1
    else: return 1
n = []
for a in range(64):
    mz = [[0 for a in g] for g in r]
    if a == 0:
        mz[st[0]][st[1]] = 1
    n.append(mz)

while not done:        
   for mz in range(len(n)):
    for x in range(1,szy):
      for y in range(1,szx):
        ni = n[mz]
        if ni[x][y] == depth:
          for s in [0,1,2,3]:          
             if r[x+m[s][0]][y+m[s][1]] == '.':
              ni = n[mz]  
              if ni[x+m[s][0]][y+m[s][1]] == 0:
                 ni[x+m[s][0]][y+m[s][1]] = depth+1
          if (x,y) in l:            
            code = l[(x,y)]
            if (code == 'ZZ') and (mz == 0):
                print ('finished',depth)
                print ('part 2 - ',x,y,code,depth)
                done = True
                printgn(r,n)
            for a in l:
              if code == l[a]:
                if a != (x,y):
                  e = edge(x,y,szx,szy)
                  if  (e == 1):
                    ni = n[mz+1]                   
                    ni[a[0]][a[1]] = depth+1
                  if (mz != 0) and (e == -1):
                    ni = n[mz-1] 
                    ni[a[0]][a[1]] = depth+1
                    
   if depth % 1000 == 0:
       for mzn in range(len(n[:5])):
           print('maze',mzn)
           printgn(r,n[mzn])
   depth += 1
    
