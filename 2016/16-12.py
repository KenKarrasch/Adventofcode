f = open('16-12.txt').read().split('\n')

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
   
for pt in [1,2]:
  if pt == 1: doreg([0,0,0,0])
  if pt == 2: doreg([0,0,1,0])
  p = 0
  while p < len(f):
    s = f[p].split()
    if 'cpy' in s:
      reg[s[2]] = gv(s[1])
    if 'jnz' in s:
      if gv(s[1]) != 0:
        p += int(s[2])-1
    if 'inc' in s:
      reg[s[1]] += 1
    if 'dec' in s:
      reg[s[1]] -= 1
    p += 1
  print 'part',pt,'-',reg['a']
