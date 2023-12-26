from collections import deque
import copy

# Very slow computation

# concept is to use relativity, i.e. assume the rock is stationary, and adjust
# the velocities of all the hails. Trial velocities in x/y/z axes, i've used -300,300 in
# all axises.  Eventually all the hails collide at the same point, the rock. (That is
# where part one calculations came in handy where the particles collide on the x/y plane
# checking for z also).  Only three hailstones were actually needed for the 
# calculations. 

# I'm pretty sure an analytical (simultaneous equations) method could be used.


f = open('23-24t.txt').read().split('\n')

ex = False

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

nvct = []
for i in vct[0:3]:    
    np = i[0][:]      
    nv = [i[1][0],i[1][1],i[1][2]]
    nvct.append([np,nv])

swp = 300
r = [-65,-86,296]
vc = []
for x in range(r[0],r[0]+1):
  print(x,'of -300 to 300')
  for i in range(len(nvct)):   
    nvct[i][1][0] = vct[i][1][0] - x              
  for y in range(r[1],r[1]+1):
    for i in range(len(nvct)):    
        nvct[i][1][1] = vct[i][1][1] - y        
    for z in range(r[2],r[2]+1):
        for i in range(len(nvct)):    
            nvct[i][1][2] = vct[i][1][2] - z            
        hit = True
        for i in range(len(nvct)):
            for j in range(i+1,len(nvct)):    
                eq1 = geteq(nvct[i])
                eq2 = geteq(nvct[j])
                ipx,ipy = intersect(eq1,eq2)
                if [ipx,ipy] != [None,None]:       
                    if nvct[i][1][0] != 0 and nvct[j][1][0] != 0:
                        t1 = (ipx - nvct[i][0][0])/nvct[i][1][0]
                        t2 = (ipx - nvct[j][0][0])/nvct[j][1][0]           
                        z1 = nvct[i][0][2] + t1 * nvct[i][1][2]
                        z2 = nvct[j][0][2] + t2 * nvct[j][1][2]    
                        if z1 != z2:                                
                            hit = False                     
                    else: 
                        hit = False
                else: hit = False
        if hit: 
            vc = [x,y,z]
            print('velocity',x,y,z)

print('part 2',int(ipx) + int(ipy) + int(z2))

