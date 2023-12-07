import math
r = open('23-7t4.txt').read().split('\n')

def gv(card):
    if card in '23456789':
        return int(card)
    if card == 'T': return 10
    if card == 'J': return 11
    if card == 'Q': return 12
    if card == 'K': return 13
    if card == 'A': return 14


v = [int(y.split()[1]) for y in r]

cds = [y.split()[0] for y in r]

#for i in range(len(v)):
    #print v[i]
    #print cds[i]
hs = []
sgs = []

   
def fv(hd):
    if hd.count(hd[0]) == 5:
     return int(math.pow(100,12))#hd[0]*int(math.pow(100,12))
    return 0

def fo(hd):
   for c in range(len(hd)):
    if hd.count(hd[c]) == 4:
     return int(math.pow(100,11))#1#hd[c]*int(math.pow(100,11))
   return 0

def fh(hd):
   tw = 0
   th = 0
   for c in range(len(hd)):
    if hd.count(hd[c]) == 2:
        tw = hd[c]
    if hd.count(hd[c]) == 3:
        th = hd[c]
   if tw > 0 and th > 0:
       return int(math.pow(100,9))#(th*100+tw)*int(math.pow(100,9))
   return 0

def thr(hd):
   for c in range(len(hd)):
    if hd.count(hd[c]) == 3:
     if fh(hd) == 0:
      return int(math.pow(100,8))#hd[c]*int(math.pow(100,8))
   return 0
          
def twpr(hd):
   pr = 0
   p1 = 0
   p2 = 0
   for c in range(len(hd)):
    #print pr,p1,p2
    if hd.count(hd[c]) == 2:
      pr += 1
      if p1 == 0:
          p1 = hd[c]
      else: p2 = hd[c]
   if pr == 4:
       #print p1,p2
       return int(math.pow(100,6))#(p1*100+p2)*int(math.pow(100,6))
   return 0
       
def pr(hd):
   #print 'pair',range(len(hd))
   for c in range(len(hd)):
    #print hd,hd.count(hd[c])
    if hd.count(hd[c]) == 2:
      #print 'pr',hd[c]
      if twpr(hd) == 0:
        if fh(hd) == 0:
         return int(math.pow(100,5))#hd[c]*int(math.pow(100,5))
   return 0

stgs = []

for h in range(len(v)):
    hd = []
    strg = 0
    for c in cds[h]:
        hd.append(gv(c))
    #hd.sort()
    hd = hd[::-1]
    hs.append(hd)
for h in range(len(v)):
    strg = 0
    o = 0
    hd = hs[h]
    for c in range(5):#[::-1]:
      #print 'c',c
      #if hd.count(hd[c]) == 1:
        strg += hd[c] * int(math.pow(100,o))
        o += 1
    strg += pr(hd)
    strg += twpr(hd)
    strg += thr(hd)
    strg += fh(hd)
    strg += fo(hd)
    strg += fv(hd)
    stgs.append([strg,h])

    #print cds[h],strg
#print stgs
stgs.sort()
#print stgs
ty = 0
for i in range(len(v)):
    #if stgs[i][0] == stgs[i+1][0]:
        #print 'double'
    #print cds[stgs[i][1]],v[stgs[i][1]],'x',(i+1),stgs[i][1]+1,stgs[i][0]
    ty += v[stgs[i][1]]*(i+1)#(stgs[i][1]+1)
print ty

# 247676080 too low
# 247149165 too low
# 247149
print len(v),'hands'

