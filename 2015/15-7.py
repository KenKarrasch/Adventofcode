f = open('15-7.txt').read().split('\n')

def getregs(d):
  ls = []
  for r in d:
   if not r[4] in ls:
    ls.append([r[4],0])
  return ls

def getls(l,ls):
  for h in range(len(ls)):
    if ls[h][0] == l:
     return(h)
     
def gv(ch,ls):
  if ch[0] in '1234567890':
    return(int(ch))
  return(ls[getls(ch,ls)][1])
       
d = []
for l in f:
  l = l.replace('NOT','0 NOT')
  if len(l.split()) == 3:
    l = l.replace('->', 'ASSIGN 0 ->')
  pts = l.split()
  d.append(pts)
ls = getregs(d)
for i in range(2):
 ip = 0
 for u in range(len(d)):
  for w in range(len(d)):
   a = gv(d[ip][0],ls)
   b = gv(d[ip][2],ls)
   e = d[ip][1]
   if e == 'ASSIGN': c = a
   if e == 'AND': c = a & b
   if e == 'OR': c = a | b
   if e == 'LSHIFT': c = a << b
   if e == 'RSHIFT': c = a >> b
   if e == 'NOT':
     c = ~b
     if c < 0:
       c += 65536
   if i == 1:
    if d[ip][4] != 'b':
     ls[getls(d[ip][4],ls)][1] = c
   else:
    ls[getls(d[ip][4],ls)][1] = c
   ip += 1
  if ip > len(ls)-1:
    ip = 0
  if i == 0:
   if d[ip][4] == 'a':
    print 'a',c
 a = ls[getls('a',ls)][1]
 print 'part',i + 1,'-',a
 ls = getregs(d)
 ls[getls('b',ls)][1] = a

