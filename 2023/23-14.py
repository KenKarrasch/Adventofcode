import copy

f = open('23-14.txt').read().split('\n')

# find the pattern, then do modulus of billion

g = []
lb = ['#' for y in range(len(f[0])+2)]

g.append(lb)
for i in f:
    ln = ['#']
    
    for j in i:
        ln.append(j)
    ln.append('#')
    g.append(ln)
    
g.append(lb[:])
    
def prg():
  for i in range(len(g)):
    ln = ''
    for j in range(min(len(g[0]),50)):
      if g[i][j] == '.':
        ln += '_'
      if g[i][j] == 'O':
        ln += 'o'
      if g[i][j] == '#':
        ln += '#'
    print ln
           
           
#prg()


def rotate():
  ng = copy.deepcopy(g)
  l = len(g)
  for i in range(l):
    for j in range(l):
      g[i][j] = ng[l-j-1][i]
    
def calcload():
 ty = 0
 for r in range(len(g)):
  for c in range(len(g[0])):
    if g[r][c] == 'O':
       ty += len(g)-r-1
 return ty

def spin():
 for r in range(len(g)):
  for c in range(len(g[0])):
    if g[r][c] == 'O':
       ht = -1
       #print 'rc',r,c
       at = False
       for i in range(1,r+1):
         #print i, g[r-i][c]
         if g[r-i][c] != '.':
            #print i,c
            if ht == -1:
              ht = i-1
       if ht != -1:
         #print r,c,ht
         g[r][c] = '.'
         g[r-ht][c] = 'O'
         #prg()
         #print'=========='
         
ptn = []

spin()
#prg()
print 'part 1',calcload() 


fd = False

sdep = 600
sf = []

for c in range(sdep):
 if c%100==0: print c
 for i in range(4):
  spin()
  rotate()
 ptn.append(calcload())
 if calcload() == 64:
      sf.append(c)
 if not fd:
   if c > 100:
    for i in range(len(ptn)-10):
     if ptn[i:i+56] == ptn[-57:-1]:
      print 'fd pattern',c
      print ptn[-50:-1]
      fd = True
 #prg()
#print 'sf',sf

#prg()
d = []

mp = 1000000
id = -1
s = sdep

for i in range(s-100,sdep):
   if ptn[s-100:s-20].count(ptn[i]) < mp:
    mp = ptn[s-100:s-20].count(ptn[i])
    id = i
    
#print 'ideal',ptn[id]

for i in range(len(ptn)):
    if ptn[i] == ptn[id]:
        d.append(i)
        
#print 'd',d

dd = []

for i in range(len(d)-1):
    dd.append(d[i+1]-d[i])

#print 'dd',dd

cycl = dd[-1]
print 'cycle',cycl


sd = 1000000000%cycl

tf = 500%cycl

#print 'b:',sd ,'500:',tf


print 'part 2',ptn[500+sd-tf:500+sd-tf+cycl][-1]


# 98101 too low

