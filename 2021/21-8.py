import itertools
# started with a deductive algorithm but gave up
# ended up brute forcing it

f = open('21-8.txt').read().split('\n')
r,ot = [],[]
for i in f:
    r.append(i.split(' | ')[0].split())
    ot.append(i.split(' | ')[1].split())
    
ct = 0
for u in ot:
  g = 0
  for j in u:
    if len(j) in [2,4,3,7]:
         g += 1
  ct += g
        
print 'part 1 -',ct
perms = [list(i) for i in itertools.permutations(range(7),7)]
dt = {} # 7 seg display
dt[0] = 'abcefg'
dt[1] = 'cf'
dt[2] = 'acdeg'
dt[3] = 'acdfg'
dt[4] = 'bcdf'
dt[5] = 'abdfg'
dt[6] = 'abdefg'
dt[7] = 'acf'
dt[8] = 'abcdefg'
dt[9] = 'abcdfg'
outn =  list(dt.values())

def rmap(l,ky):
    cd = ord(l)
    for rl in range(len(ky)):
      if cd == ky[rl]+ord('a'):
        return chr(rl+ord('a'))
    
def vld(cdt):      
  for w in cdt:
    fd = False
    for u in outn:
      if sorted(w) == sorted(u): fd = True    
    if not fd: return False
  return True
    
tot = 0
for i in range(len(r)):  
  for mp in perms: 
    dn = False
    if not dn: 
        np,nr = list(mp),[]      
        for h in r[i]:
            ns = ''
            for c in h:
                ns += rmap(c,np)
            nr.append(ns)          
        if vld(nr):
            dn = True
            wn = np[:] 
  np = wn[:]  
  num = 0
  for h in ot[i]:
    ns = ''
    for c in h: ns += rmap(c,np)  
    for j in range(len(outn)):
        if sorted(outn[j]) == sorted(ns): num = j + num*10       
  tot += num
  print i,'of',len(r)
print 'part 2 -',tot
