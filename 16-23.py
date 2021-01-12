import copy

f = open('16-23.txt').read().split('\n')

iin = []

for b in f:
    iin.append(b.split())
    
ao = ord('a')
zo = ord('z')

reg = {}

def doreg(rs):
 reg['a'] = rs[0]
 reg['b'] = rs[1]
 reg['c'] = rs[2]
 reg['d'] = rs[3]

def gv(c):
   if ord(c[0]) >= ao:
     if ord(c[0]) <= zo:
        return reg[c]
   return int(c)
   
def lst():
   for istr in i:
      print istr
   
m = 1

for g in range(1,13)[::-1]:
    m *= g
    print m,g-1

ring = 4
ctr = 0
for pt in [1]:
  if pt == 1: doreg([5,0,0,0])
  if pt == 2: doreg([12,0,0,0])
  p = 0
  i = copy.deepcopy(iin)
  while p < len(i):
    s = i[p]
    #print s
    if 'cpy' in s:
      reg[s[2]] = gv(s[1])
      if s[2] == 'd':
       if (reg['a'] == reg['d']) and (reg['c'] == -16):
        print ctr, reg
        amp = 1
        #lst()
        if amp == 0:
         while reg['b'] > 0:
            fa = reg['b']
            reg['a'] *= fa
            reg['d'] *= fa
            reg['b'] -= 1
            print ctr, reg
        #ring = 9000
    if 'jnz' in s:
      if gv(s[1]) != 0:
        p += int(gv(s[2]))-1
    if 'inc' in s:
      reg[s[1]] += 1
    if 'dec' in s:
      reg[s[1]] -= 1
    if 'tgl' in s:
     if gv(s[1])+p < len(i):
      ist = i[gv(s[1])+p]
      c = ist[0]
      if len(ist) == 2:
        if c == 'inc': 
           o = 'dec'
        else:
           o = 'inc'
      if len(ist) == 3:
        if c == 'jnz': 
           o = 'cpy'
        else:
           o = 'jnz'
      i[gv(s[1])+p][0] = o
    p += 1
    #print p
    if ctr%1==0:
      if ctr < 10:
        print ctr,reg
    #if ring > 0:
       #print ctr,reg
    ring -= 1
    ctr += 1

    #print ''
  print 'part',pt,'-',reg['a']
