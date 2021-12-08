import itertools

f = open('21-8.txt').read().split('\n')
r,ot = [],[]
for i in f:
    r.append(i.split(' | ')[0].split())
    ot.append(i.split(' | ')[1].split())
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
        np,nr = list(mp),nr        
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
  print(i,'of',len(r))
print(tot)
