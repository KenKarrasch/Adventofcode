r = open('23-6.txt').read().split('\n')

# little bit surpised the brute force 
# approach computed so fast, was bracing
# myself for doing some complex algorithm work

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
  for td in range(t[tt]):
    if getdist(td,t[tt]) > d[tt]:
      s += 1
  f *= s
  
print 'part 2', f
