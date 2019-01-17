f  = open('18-24.txt').read()
# straightforward solution, nothing groundbreaking.  The lesson in day 24 is the importance of having a clear and \
# unambiguous specification.
# This is a general solution.

armies = f.split('Infection')
BLUDGEON = 1
SLASHING = 2
RADIATION = 3
FIRE = 4
COLD = 5

def bl(str):
    return 'bludgeon' in str
def sl(str):
    return 'slashing' in str
def rad(str):
    return 'radiation' in str
def fire(str):
    return 'fire' in str
def cold(str):
    return 'cold' in str
def gmd(str):
    if 'weak' in str:
      return 'weak'
    if 'immune' in str:
      return 'immune'
    
immleg,infleg = [],[]

def getarmies(legion,imm,boost):
 units,hp,init,damage, \
 dtype,arm,sts,sts2 = \
 [],[],[],[],[],[],[],[]
 arm = -1
 immw = imm.split()
 for h in range(len(immw)):
  if immw[h] == 'units':
    sts.append(h)
 for h in range(len(imm)-5):
  if imm[h:h+5] == 'units':
    sts2.append(h)
 for st in sts:
    units.append(int(immw[st-1]))
    hp.append(int(immw[st+3]))
 for h in range(len(immw)):
  if immw[h] == 'initiative':
    init.append(int(immw[h+1]))
  if immw[h] == 'damage':
    damage.append( \
      int(immw[h-2])+boost)
    dtype.append(immw[h-1])
 dam = imm.split('(')
 pow = []
 while arm < len(sts)-1:
  arm += 1
  str = []
  if arm != len(sts)-1:
    frag = imm[sts2[arm]:sts2[arm+1]]
  else:
    frag = imm[sts2[arm]:]
  if '(' not in frag:
   str.append([])
  else:
   h = frag.split(')')[0].split('(')[1].split(';')
   for pt in h:
    gh = pt.split(' to ')
    j = gh[1]
    str.append([gmd(gh[0]) \
      ,bl(j),sl(j) \
      ,rad(j),fire(j),cold(j)])
  pow.append(str)
 for l in range(len(units)):
   ddpow = []
   for u in pow[l]:
     ddpow.append(u[:])
   legion.append([units[l],hp[l], \
      ddpow,damage[l], \
      dtype[l],init[l]])
   
def targetselection(leg):
  o = []
  for l in range(len(leg)):
    o.append([l, \
    leg[l][0]*leg[l][3], \
    leg[l][5], \
    leg[l][1]])
  s = sorted(o, \
  key = lambda x:(x[1], \
      x[2]),reverse = True)
  out = []
  for h in s:
    out.append(h[0])
  return out
  
def getresiliance(md,df):
  if md == 'bludgeoning':
    return df[BLUDGEON]
  if md == 'slashing':
    return df[SLASHING]
  if md == 'radiation':
    return df[RADIATION]
  if md == 'fire':
    return df[FIRE]
  if md == 'cold':
    return df[COLD]
  
def potdamage(ar,t):
  md = ar[4]
  d = ar[3]*ar[0]
  if len(t) > 0:
   for df in t[2]:
    if len(df) > 0:
     if 'immune' in df[0]:
      if getresiliance(md,df):
        d = 0
     if 'weak' in df[0]:
      if getresiliance(md,df):
        d *= 2
  return d
    
def attacksel(tgts,ar,en):
 tgtcans = []
 taken = [False] * len(en)
 for tg in tgts:
   can = []
   for e in range(len(en)):
    if not taken[e] and en[e][1]>0:
     t = en[e]
     if potdamage(ar[tg],t) > 0:
      if t[0]*t[3] > 0:
       can.append( \
         [potdamage(ar[tg],t), \
         t[0]*t[3],t[5],e])
   can = sorted(can, \
     key = lambda x: \
      (x[0],x[1],x[2]), \
      reverse = True)
   if len(can) > 0:
    if can[0][0] != 0:
     taken[can[0][3]] = True
   tgtcans.append(can)
 return tgtcans
 
def kill(a,tg):
  d = potdamage(a,tg)
  tg[0] -= int(d/tg[1])
  
def getnum(ls,g):
    for l in range(len(ls)):
      if ls[l] == g:
          return l
    
def doatk(a1,a2,inf,imm,timm,tinf):
  c = len(inf)+len(imm)+1
  while c > 0:
    c -= 1
    for g in range(len(inf)):
      if inf[g][5] == c and \
         inf[g][0]>0:
       tg = getnum(tinf,g)
       if len(a2[tg]) > 0:
        kill(inf[g],imm[a2[tg][0][3]])
    for g in range(len(imm)):
      if imm[g][5] == c and \
         imm[g][0]>0:
       tg = getnum(timm,g)
       if len(a1[tg]) > 0:
        kill(imm[g],inf[a1[tg][0][3]])
        
def countarmies(ar):
    tt = 0
    for g in ar:
       if g[0] > 0:
           tt += g[0]
    return tt

found = False
boost = -1
pt1 = False
while not found:
 boost += 1
 immleg = []
 infleg = []
 getarmies(immleg,armies[0],boost)
 getarmies(infleg,armies[1],0)
 previmm = 0
 previnf = 0
 #loop = False
 #loop2 = False
 #debug = False
 tie = False
 while countarmies(immleg) > 0 and \
   countarmies(infleg) > 0 and \
   not tie:
    timm = targetselection(immleg)
    atksimm = attacksel( \
     timm,immleg,infleg)
    tinf = targetselection(infleg)
    atksinf = attacksel( \
    tinf,infleg,immleg)
    doatk(atksimm, \
     atksinf,infleg, \
     immleg,timm,tinf)
    imc = countarmies(immleg)
    ifc = countarmies(infleg) 
    if previmm == imc:
      if previnf == ifc:
        tie = True
    previmm = imc
    previnf = ifc

 if not pt1:
  print 'part 1 -',countarmies(infleg)
  print 'part 2 searchng...'
  pt1 = True
 if countarmies(infleg) == 0:
  print 'part 2 -',countarmies(immleg) 
  found = True

