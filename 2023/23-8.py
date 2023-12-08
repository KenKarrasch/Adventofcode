import re
import math
# working out the cycles, then lcm

r = open('23-8.txt').read().split('\n\n')

inst = 0

def mv(l,d):
    
    if d == 'L':
        return 

gps = {}
ds = r[0]
for i in r[1].split('\n'):
    dr = i.split(' = ')
    regex = '[A-Z]+'
    pl = re.findall(regex,dr[1])
    gps[dr[0]] = pl

l = 'AAA'

stp = 0
while l not in 'ZZZ':
    if ds[inst] == 'L':
      l = gps[l][0]
    else:
      l = gps[l][1]
    inst = (inst+1)%len(ds)
    stp += 1
print 'part 1',stp

stp = 0

pls = []

for i in list(gps.keys()):
    if i[2] == 'A':
        pls.append(i)

dn = False
cylc = []*len(pls)
for i in range(len(pls)):
    cylc.append(0)

while not dn:
  for i in range(len(pls)):
    l = pls[i]
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
  if cylc.count(0) == 0:
        dn = True

    
def lcm(x, y):
    from fractions import gcd 
    # or can import gcd from `math` in Python 3
    return x * y // gcd(x, y)

lm = cylc[0]
for i in cylc:
    lm = lcm(lm,i)

print 'part 2',lm
