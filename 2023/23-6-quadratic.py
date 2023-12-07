import math
r = open('23-6.txt').read().split('\n')

# little bit surpised the brute force 
# approach computed so fast, 
# (2-3 secs on the iphone), was bracing
# myself for doing some complex algorithm work

# update: added quadratic method for
# fun

t,d = [[int(z) for z in y.split(':')[1].split()] for y in r]

def getdist(delay,time):
    return (time-delay)*delay

f = 1

for tt in range(len(t)):
  s = 0
  for td in range(t[tt]):
    if getdist(td,t[tt]) > d[tt]:
      s += 1
  f *= s
  
print 'part 1', f

nt,nd = '',''

for i in range(len(t)):
  nt += str(t[i])
  nd += str(d[i])
t = [int(nt)]
d = [int(nd)]

f = 1

for tt in range(len(t)):
  s = 0
  print t[tt]
  
  dst = d[tt]
  tm = t[tt]
  print 'dst,tm',dst,tm
    # dst = (tm - del) * del
    # dst = tm*del - del^2
    # 0 = tm*del - del^2 - dst
  a = -1
  b = tm
  c = -dst
  print 'a,b,c', a, b, c
  se = (-b+math.sqrt((b*b) - (4*a*c)))/(2*a) 
  te = (-b-math.sqrt((b*b) - (4*a*c)))/(2*a)
  print 'quadratic',int(te)-int(se)
  for td in range(t[tt]):
    #if td%1000000==0: print td
    if getdist(td,t[tt]) > d[tt]:
      s += 1
  print 'brute force',s
  f *= s
  
print 'part 2', f
