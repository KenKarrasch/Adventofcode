
from collections import deque

f = open('23-24.txt').read().split('\n')

ex = False

#print(f)
vct = []
for i in f:
    pi,vi = i.split(' @ ')
    p = [int(y) for y in pi.split(',')]
    v = [int(y) for y in vi.split(',')]
    vct.append([p,v])

def geteq(v):
    p1 = v[0][:]
    p2 = [v[0][0] + v[1][0], v[0][1] + v[1][1], v[0][2] + v[1][2]]   
    x1,y1,x2,y2 = p1[0],p1[1],p2[0],p2[1]          
    A,B,C = y2-y1,x1-x2,y1*(x2-x1) - (y2-y1)*x1
    return ([A,B,C])

def intersect(eq1,eq2):
    a1,a2,b1,b2,c1,c2 = eq1[0],eq2[0],eq1[1],eq2[1],eq1[2],eq2[2]
    if (a1*b2 - a2*b1) != 0:
      ipx = (b1*c2 - b2*c1) / (a1*b2 - a2*b1)
      ipy = (a2*c1 - a1*c2) / (a1*b2 - a2*b1)
      return [ipx,ipy]
    return [None,None]
       
ty = 0
for i in range(len(vct)):
  for j in range(i+1,len(vct)):    
    #print(i,j)
    eq1 = geteq(vct[i])
    eq2 = geteq(vct[j])
    #print(eq1,eq2)
    ipx,ipy = intersect(eq1,eq2)
    if [ipx,ipy] != [None,None]:       
       #vct[0][0] + t * vct[1][0] = ipx       
       t1 = (ipx - vct[i][0][0])/vct[i][1][0]
       t2 = (ipx - vct[j][0][0])/vct[j][1][0]       
       if t1 > 0 and t2 > 0:        
        if not ex:
         if 200000000000000 < ipx < 400000000000000:
           if 200000000000000 < ipy < 400000000000000:
              #print(vct[i],vct[j],ipx,ipy)
              ty += 1
        if ex:
          if 7 < ipx < 27:
           if 7 < ipy < 27:
              #print('success',vct[i],vct[j],ipx,ipy)
              ty += 1        

print('part 1',ty)         

rck = '24, 13, 10 @ -3, 1, 2'


# 200000000000000
# 222734229484956
   
# 761691907059631
    # 38827 too high
