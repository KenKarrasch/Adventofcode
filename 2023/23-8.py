import re
import math
# workout the cycles

r = open('23-8.txt').read().split('\n\n')

inst = 0

def mv(l,d):
    if d == 'L':
        return 

gps = {}
#print r
ds = r[0]
for i in r[1].split('\n'):
    dr = i.split(' = ')
    #print dr
    regex = '[A-Z]+'
    pl = re.findall(regex,dr[1])
    #pl = re.compile(dr[1])
    #print 'pl',pl
    gps[dr[0]] = pl
#print gps

l = 'AAA'
stp = 0

pls = []

for i in list(gps.keys()):
    if i[2] == 'A':
        pls.append(i)

print pls

dn = False
cylc = []*len(pls)
for i in range(len(pls)):
    cylc.append(0)
    



while not dn:#l not dn:#in 'ZZZ':
  for i in range(len(pls)):
    l = pls[i]
    #print inst,l,ds[inst]
    if ds[inst] == 'L':
      l = gps[l][0]
    else:
      l = gps[l][1]
    pls[i] = l
  inst = (inst+1)%len(ds)
  stp += 1
  for i in range(len(pls)):
    if pls[i][2] == 'Z':
       if cylc[i] == 0:
           cylc[i] = stp
           print cylc
  #print cylc.count(0)
  if cylc.count(0) == 0:
        print 'done'
        dn = True
  if stp%100000 == 0:
      print stp,pls
print cylc,'done'

    
def lcm(x, y):
    from fractions import gcd 
    # or can import gcd from `math` in Python 3
    return x * y // gcd(x, y)


#print math.lcm(cylc)
lm = cylc[0]
for i in cylc:
    lm = lcm(lm,i)

print lm

